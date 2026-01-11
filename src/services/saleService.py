from datetime import datetime, timedelta
from src.domain.models.Orders import Order, Product_Order
from src.domain.models.Sales import Sale
from src.infrastructure.db.repositories.sale_repository_sqlalchemy import SaleRepositorySQLAlchemy

class SaleService:

    def __init__(self, saleRepo: SaleRepositorySQLAlchemy):
        self.repository = saleRepo

    '''Evaluar como puedo hacer las cosas, ya que para castear una venta necesito una orden y para una orden necesito una lista de productos'''
    def _map_db_sale_to_domain(self, db_sale) -> Sale:
        return Sale(
            id=db_sale.id,
            order=Order(
                id=db_sale.order.id, 
                employee_id=db_sale.order.employee_id, 
                table_id=db_sale.order.table_id, 
                products=[Product_Order(
                    product_id=po.product_id, 
                    quantity=po.quantity, 
                    price=po.price) for po in db_sale.order.products], 
                start_at=db_sale.order.start_at, 
                last_updated=db_sale.order.last_updated),
            payment_method=db_sale.payment_method,
            recorded_at=db_sale.recorded_at,
            taxes=db_sale.taxes
        )
    
    def get_by_id_with_order(self, sale_id: int) -> Sale | None:
        db_sale = self.repository.get_by_id_with_order(sale_id)
        if not db_sale:
            return None
        return self._map_db_sale_to_domain(db_sale)
    
    def get_by_order_id_with_order(self, order_id: int) -> Sale | None:
        db_sale = self.repository.get_by_order_id_with_order(order_id)
        if not db_sale:
            return None
        return self._map_db_sale_to_domain(db_sale)
    
    def get_by_invoice_id_with_order(self, invoice_id: int) -> Sale | None:
        db_sale = self.repository.get_by_invoice_id_with_order(invoice_id)
        if not db_sale:
            return None
        return self._map_db_sale_to_domain(db_sale)
    
    def get_all_by_specific_date_with_order(self, inicial_date:datetime, final_date:datetime) -> list[Sale]:
        if inicial_date >= final_date:
            raise ValueError("la fecha inicial debe ser anterior a la fecha final")
        if final_date > inicial_date + timedelta(days=30):
            raise ValueError("el registro maximo es de 30 dias entre la fecha inicial y final")
        if final_date > datetime.now():
            raise ValueError("la fecha final no puede ser mayor a la fecha actual")
        
        db_sales = self.repository.get_all_by_specific_date_with_order(inicial_date, final_date)
        return [self._map_db_sale_to_domain(db_sale) for db_sale in db_sales]
    
    def create(self, sale: Sale) -> Sale:
        db_sale = self.repository.create(sale)
        return sale
    
    def update(self, sale: Sale) -> Sale:
        db_sale = self.repository.update(sale)
        if not db_sale:
            raise ValueError(f"La venta con id {sale.id} no existe")
        return self._map_db_sale_to_domain(db_sale)
    
    def delete(self, sale_id: int) -> None:
        db_sale = self.repository.delete(sale_id)
        if not db_sale:
            raise ValueError(f"La venta con id {sale_id} no existe")
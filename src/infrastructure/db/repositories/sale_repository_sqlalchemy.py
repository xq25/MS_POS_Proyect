from src.infrastructure.db.models.orderModel import OrderModel
from src.infrastructure.db.models.saleModel import SaleModel
from src.domain.models.Sales import Sale
from sqlalchemy.orm import Session, joinedload

class SaleRepositorySQLAlchemy:
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id_with_order(self, sale_id: int)->SaleModel | None:
        db_sale =  self.db.query(SaleModel).options(
            joinedload(SaleModel.order).joinedload("products")
        ).filter(SaleModel.id == sale_id).first()
        if not db_sale:
            return None
        return db_sale
    
    def get_by_order_id_with_order(self, order_id: int)->SaleModel | None:
        db_sale =  self.db.query(SaleModel).options(
            joinedload(SaleModel.order).joinedload("products")
        ).filter(SaleModel.order_id == order_id).first()
        if not db_sale:
            return None
        return db_sale
    
    def get_by_invoice_id_with_order(self, invoice_id: int)->SaleModel | None:
        db_sale =  self.db.query(SaleModel).options(
            joinedload(SaleModel.order).joinedload("products")
        ).filter(SaleModel.invoice.has(id=invoice_id)).first()
        if not db_sale:
            return None
        return db_sale
    
    def get_all_by_specific_date_with_order(self, inicial_date, final_date)->list[SaleModel]:
        db_sales = self.db.query(SaleModel).options(
            joinedload(SaleModel.order).joinedload("products")
        ).filter(SaleModel.recorded_at >= inicial_date and SaleModel.recorded_at < final_date).all()
        if not db_sales:
            return []
        return db_sales

    def create(self, sale: Sale):
        db_sale = SaleModel(
            order_id=sale.order.id,
            payment_method=sale.payment_method.value,
            recorded_at=sale.recorded_at,
            total_amount=sale.total_amount,
            taxes=sale.taxes
        )
        self.db.add(db_sale)
        return db_sale
    
    def update(self, sale: Sale):
        db_sale = self.get_by_id(sale.id)
        if not db_sale:
            return None
        db_sale.order_id = sale.order.id
        db_sale.payment_method = sale.payment_method.value
        db_sale.recorded_at = sale.recorded_at
        db_sale.total_amount = sale.total_amount
        db_sale.taxes = sale.taxes
        return db_sale
    
    def delete(self, sale_id: int):
        db_sale = self.get_by_id(sale_id)
        if not db_sale:
            return None
        self.db.delete(db_sale)
        return db_sale
from sqlalchemy.orm import Session, joinedload
from src.domain.models.Orders import Order
from src.infrastructure.db.models.orderModel import OrderModel
from src.infrastructure.db.models.orderProductModel import OrderProductModel

class OrderRepositorySQLAlchemy:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(OrderModel).all()
    
    def get_by_id(self, order_id: int):
        return self.db.query(OrderModel).filter(OrderModel.id == order_id).first()
    def get_by_id_with_products(self, order_id: int):
        return self.db.query(OrderModel).options(joinedload(OrderModel.products)).filter(OrderModel.id == order_id).first()
    
    def get_by_all_table_id_open_orders(self, table_id: int)-> list[OrderModel]:
        return self.db.query(OrderModel).filter(OrderModel.table_id == table_id).filter(OrderModel.sale == None).all()
    def get_by_all_table_id_open_orders_with_products(self, table_id: int)-> list[OrderModel]:
        return self.db.query(OrderModel).options(joinedload(OrderModel.products)).filter(OrderModel.table_id == table_id).filter(OrderModel.sale == None).all()
    
    def get_all_by_employee_id(self, employee_id: int):
        return self.db.query(OrderModel).filter(OrderModel.employee_id == employee_id).all()
    def get_all_by_employee_id_open_orders(self, employee_id: int):
        return self.db.query(OrderModel).filter(OrderModel.employee_id == employee_id).filter(OrderModel.sale == None).all()
    def get_all_by_employee_id_open_orders_with_products(self, employee_id: int):
        return self.db.query(OrderModel).options(joinedload(OrderModel.products)).filter(OrderModel.employee_id == employee_id).filter(OrderModel.sale == None).all()
    
    def get_all_open_orders(self):
        return self.db.query(OrderModel).filter(OrderModel.sale == None).all()
    def get_all_open_orders_with_products(self):
        return self.db.query(OrderModel).options(joinedload(OrderModel.products)).filter(OrderModel.sale == None).all()
    
    # Validar si es necesario validar el last_updated
    def get_all_by_date_range(self, start_date, end_date):
        return self.db.query(OrderModel).filter(OrderModel.start_at >= start_date and OrderModel.last_updated <= end_date).all()
    def get_all_by_date_range_with_products(self, start_date, end_date):
        return self.db.query(OrderModel).options(joinedload(OrderModel.products)).filter(OrderModel.start_at >= start_date and OrderModel.last_updated <= end_date).all()
    
    def create(self, order: Order)-> OrderModel:
        db_order = OrderModel(
            employee_id=order.employee_id,
            total_amount=order.total_amount,
            table_id=order.table_id,
            start_at=order.start_at,
            last_updated=order.last_updated,
            products = [OrderProductModel(product_id=p.product_id, quantity=p.quantity, price = p.price) for p in order.products]
        )
        self.db.add(db_order)
        return db_order
    
    def update(self, order: Order)-> OrderModel:
        db_order = self.db.query(OrderModel).get(order.id)

        if not db_order:
            return None
        
        db_order.employee_id = order.employee_id
        db_order.total_amount = order.total_amount
        db_order.table_id = order.table_id
        db_order.start_at = order.start_at
        db_order.last_updated = order.last_updated

        db_order.products.clear()
        
        for p in order.products:
            db_order.products.append(OrderProductModel(product_id=p.product_id, quantity=p.quantity, price = p.price))

        return db_order
    
    def delete(self, order_id: int):
        db_order = self.db.query(OrderModel).get(order_id)
        if db_order:
            self.db.delete(db_order)
            return db_order
        return None
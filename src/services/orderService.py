from src.domain.models.Orders import Order, Product_Order
from src.infrastructure.db.repositories.order_repository_sqlalchemy import OrderRepositorySQLAlchemy
class OrderService:
    def __init__(self, orderRepo: OrderRepositorySQLAlchemy):
        self.repository = orderRepo

#   General orders
    '''This function can we use to get all orders without products details, maybe to show a list of orders in development mode'''
    def get_all(self):
        db_orders = self.repository.get_all()
        return [
            Order(
                id=o.id,
                employee_id=o.employee_id,
                table_id=o.table_id,
                products=[], # Manage products separately in individual methods (get_by_id_xxxx_with_products)
                total_amount=o.total_amount,
                start_at=o.start_at,
                last_updated=o.last_updated
            ) for o in db_orders
        ]
    
#   Specific orders
    '''This function can we use to get an order by id without products details, maybe to show a list of orders easily'''
    def get_by_id(self, order_id: int):
        db_order = self.repository.get_by_id(order_id)
        if not db_order:
            return None
        return Order(
            id=db_order.id,
            employee_id=db_order.employee_id,
            table_id=db_order.table_id,
            products=[], # Manage products separately in individual methods (get_by_id_xxxx_with_products)
            total_amount=db_order.total_amount,
            start_at=db_order.start_at,
            last_updated=db_order.last_updated
        )
    
    '''This function can we use to get an order by id with products details'''
    def get_by_id_with_products(self, order_id: int):
        db_order = self.repository.get_by_id_with_products(order_id)
        if not db_order:
            return None
        return Order(
            id=db_order.id,
            employee_id=db_order.employee_id,
            table_id=db_order.table_id,
            products=[Product_Order(product_id=p.product_id, quantity=p.quantity, price=p.price) for p in db_order.products],
            total_amount=db_order.total_amount,
            start_at=db_order.start_at,
            last_updated=db_order.last_updated
        )
    
    '''This function can we use to get all orders by table id without products details but only open orders (without sale associated)'''
    def get_all_by_table_id_open_orders(self, table_id: int):
        db_orders = self.repository.get_by_all_table_id_open_orders(table_id)
        return [
            Order(
                id=o.id,
                employee_id=o.employee_id,
                table_id=o.table_id,
                products=[], # Manage products separately in individual methods (get_by_id_xxxx_with_products)
                total_amount=o.total_amount,
                start_at=o.start_at,
                last_updated=o.last_updated
            ) for o in db_orders
        ]
    
    '''This function can we use to get all orders by table id with products details but only open orders (without sale associated)'''
    def get_all_by_table_id_with_products(self, table_id: int):
        db_orders = self.repository.get_by_all_table_id_with_products(table_id)
        return [
            Order(
                id=o.id,
                employee_id=o.employee_id,
                table_id=o.table_id,
                products=[Product_Order(product_id=p.product_id, quantity=p.quantity, price=p.price) for p in o.products],
                total_amount=o.total_amount,
                start_at=o.start_at,
                last_updated=o.last_updated
            ) for o in db_orders
        ]
    
    '''This function can we use to get all orders by employee id without products details, maybe to validate employee performance'''
    def get_all_by_employee_id(self, employee_id: int):
        db_orders = self.repository.get_all_by_employee_id(employee_id)
        return [
            Order(
                id=o.id,
                employee_id=o.employee_id,
                table_id=o.table_id,
                products=[], # Manage products separately in individual methods (get_by_id_xxxx_with_products)
                total_amount=o.total_amount,
                start_at=o.start_at,
                last_updated=o.last_updated
            ) for o in db_orders
        ]
    
    '''This function can we use to get all open orders by employee id without products details, maybe to validate employee performance'''
    def get_all_by_employee_id_open_orders(self, employee_id: int):
        db_orders = self.repository.get_all_by_employee_id_open_orders(employee_id)
        return [
            Order(
                id=o.id,
                employee_id=o.employee_id,
                table_id=o.table_id,
                products=[], # Manage products separately in individual methods (get_by_id_xxxx_with_products)
                total_amount=o.total_amount,
                start_at=o.start_at,
                last_updated=o.last_updated
            ) for o in db_orders
        ]

    '''This function can we use to get all open orders by employee id with products details, maybe to validate employee performance'''
    def get_all_by_employee_id_open_orders_with_products(self, employee_id: int):
        db_orders = self.repository.get_all_by_employee_id_open_orders_with_products(employee_id)
        return [
            Order(
                id=o.id,
                employee_id=o.employee_id,
                table_id=o.table_id,
                products=[Product_Order(product_id=p.product_id, quantity=p.quantity, price=p.price) for p in o.products],
                total_amount=o.total_amount,
                start_at=o.start_at,
                last_updated=o.last_updated
            ) for o in db_orders
        ]
    
    '''This function can we use to get all open orders without products details, maybe to show a list of open orders in development mode'''
    def get_all_open_orders(self):
        db_orders = self.repository.get_all_open_orders()
        return [
            Order(
                id=o.id,
                employee_id=o.employee_id,
                table_id=o.table_id,
                products=[], # Manage products separately in individual methods (get_by_id_xxxx_with_products)
                total_amount=o.total_amount,
                start_at=o.start_at,
                last_updated=o.last_updated
            ) for o in db_orders
        ]
    
    '''This function can we use to get all open orders with products details'''
    def get_all_open_orders_with_products(self):
        db_orders = self.repository.get_all_open_orders_with_products()
        return [
            Order(
                id=o.id,
                employee_id=o.employee_id,
                table_id=o.table_id,
                products=[Product_Order(product_id=p.product_id, quantity=p.quantity, price=p.price) for p in o.products],
                total_amount=o.total_amount,
                start_at=o.start_at,
                last_updated=o.last_updated
            ) for o in db_orders
        ]

    '''This function can we use to get all orders by date range without products details, maybe to show a report of orders in development mode or validate actually orders of especific time'''
    def get_all_by_date_range(self, start_date, end_date):
        db_orders = self.repository.get_all_by_date_range(start_date, end_date)
        return [
            Order(
                id=o.id,
                employee_id=o.employee_id,
                table_id=o.table_id,
                products=[], # Manage products separately in individual methods (get_by_id_xxxx_with_products)
                total_amount=o.total_amount,
                start_at=o.start_at,
                last_updated=o.last_updated
            ) for o in db_orders
        ]
    
    '''This function can we use to get all orders by date range with products details, maybe to show a report of orders in development mode or validate actually orders of especific time'''
    def get_all_by_date_range_with_products(self, start_date, end_date):
        db_orders = self.repository.get_all_by_date_range_with_products(start_date, end_date)
        return [
            Order(
                id=o.id,
                employee_id=o.employee_id,
                table_id=o.table_id,
                products=[Product_Order(product_id=p.product_id, quantity=p.quantity, price=p.price) for p in o.products],
                total_amount=o.total_amount,
                start_at=o.start_at,
                last_updated=o.last_updated
            ) for o in db_orders
        ]
    
    @staticmethod
    def add_product_to_order(order: Order, product:Product_Order):
        ''' Actualizamos el valor de la cantidad de un producto en base a en nuevo valor que viene desde el frontend
        '''
        for p in order.products:
            if p.product_id == product.product_id:
                p.quantity = product.quantity
                return OrderService.update(order)
        
        order.products.append(product)
        return OrderService.update(order)

    @staticmethod
    def add_unit_product_to_order(order: Order, product_id:int):

        for p in order.products:
            if p.product_id == product_id:
                p.quantity +=1
                return OrderService.update(order)
        raise ValueError(f'El producto {product_id} no existe con anterioridad en la orden {order.id}')
    
    @staticmethod
    def subst_unit_product_to_order(order: Order, product_id:int):

        for i,p in enumerate(order.products):
            if p.product_id == product_id:
                p.quantity -= 1
                if p.quantity <= 0: 
                    order.products.remove(i)
                return OrderService.update(order)
            
        raise ValueError(f'El producto {product_id} no existe con anterioridad en la orden {order.id}')
    
    @staticmethod   
    def update_product_quantity_in_order(order: Order, product_id:int, quantity:int):

        for p in order.products:
            if p.product_id == product_id:
                p.quantity = quantity
                return OrderService.update(order)
            
        raise ValueError (f'No se encontro el producto con ID {product_id}, dentro de la orden {order.id}')
    
    @staticmethod
    def delete_product_to_order(order: Order, product_id:int):

        for i,p in enumerate(order.products):
            if p.product_id == product_id:
                order.products.pop(i)
                return OrderService.update(order)
            
        raise ValueError (f'No se encontro el producto con ID {product_id}, dentro de la orden {order.id}')

    def create(self, order: Order):
        db_order = self.repository.create(order)
        return Order(
            id=db_order.id,
            employee_id=db_order.employee_id,
            table_id=db_order.table_id,
            products=[Product_Order(product_id=p.product_id, quantity=p.quantity, price=p.price) for p in db_order.products],
            total_amount=db_order.total_amount,
            start_at=db_order.start_at,
            last_updated=db_order.last_updated
        )

    def update(self, order: Order):
        '''Actualizar orden en la base de datos'''
        db_order = self.repository.update(order)
        if not db_order:
            raise ValueError(f'La orden con ID {order.id} no existe')
        new_total = OrderService.calculate_total_amount(order)
        return Order(
            id=db_order.id,
            employee_id=db_order.employee_id,
            table_id=db_order.table_id,
            products=[Product_Order(product_id=p.product_id, quantity=p.quantity, price=p.price) for p in db_order.products],
            total_amount=new_total,
            start_at=db_order.start_at,
            last_updated=db_order.last_updated
        )


    def delete(self, order_id:int):
        '''Eliminar orden de la base de datos'''
        db_orderDeleted = self.repository.delete(order_id)
        if not db_orderDeleted:
            raise ValueError(f'La orden con ID {order_id} no existe')
        return 
    
    @staticmethod
    def calculate_total_amount(order: Order):
        total = 0

        for p in order.products:
            total += (p.price * p.quantity)
            #Si vamos a agregar un modulo de promociones aqui se deberia de descontar llegado el caso y tambian habria que hacer una funcion de validar si la orden aplica a una promocion
        return total

    def pay_order(order:Order):
        '''Llamar al servicio de SaleService'''
        pass
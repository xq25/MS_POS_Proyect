from src.domain.models.Orders import Order, Product_Order
class OrderService:

    def add_product_to_order(order: Order, product:Product_Order):
        code = 'order:001'
        ''' DEFINIR PRIMERO SI SOLO VAMOS A ACTUALIZAR EL VALOR DE CANTIDAD POR EEL QUE VENGA DENTRO DE PRODUCT_ORDER O SUMARLO A LA CANTIDAD TOTAL
        Validations 
            1.product exist?'''

        for p in order.products:
            if p.product_id == product.product_id:
                p.quantity += product.quantity
                return order
        
        order.products.append(product)
        return order
    
    def subst_product_to_order(order: Order, product:Product_Order):
        '''Validations 
            1.product exist?'''
        for p,i in enumerate(order.products):
            if p.product_id == product.product_id:
                p.quantity -= product.quantity
                if p.quantity <= 0: 
                    order.products.remove(i)
                return order
        raise ValueError(f'El producto {product.id} no existe con anterioridad en la orden {order.id}')

        
    
    def delete_product_to_order(order: Order, product_id:int):
        code = 'order:002'
        '''Validations 
            1.product exist?'''

        for p,i in enumerate(order.products):
            if p.product_id == product_id:
                order.products.remove(i)
                return  order
        raise ValueError (f'No se encontro el producto con ID {product_id}, dentro de la orden {order.id}')

    def create(order: Order):
        '''Crear orden en la dataBase'''
        pass

    def update(order_id:int, order: Order):
        '''Actualizar orden en la base de datos'''

    def delete(order_id:int):
        '''Eliminar orden de la base de datos'''

    def calculate_total_price(order: Order):
        total = 0

        for p in order.products:
            total += (p.price * p.quantity)
            #Si vamos a agregar un modulo de promociones aqui se deberia de descontar llegado el caso y tambian habria que hacer una funcion de validar si la orden aplica a una promocion
        return total

    def pay_order(order:Order):
        '''Llamar al servicio de SaleService'''
        pass
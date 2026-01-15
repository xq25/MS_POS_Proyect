from enum import Enum
from src.domain.models.Invoices import Client_Info, Invoice, InvoiceItem
from src.domain.models.Sales import Sale
from datetime import datetime
from src.infrastructure.db.repositories.invoice_repository_sqlalchemy import InvoiceRepositorySQLAlchemy

class InvoiceService:

    def __init__(self, invoice_repository: InvoiceRepositorySQLAlchemy):
        self.repository = invoice_repository

    def _generate_invoice_number(self) -> str:
        # Placeholder logic for generating a unique invoice number
        return f"INV-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"

    '''This function generate a default invoice from a ticket/sale'''
    def generate_invoice(self, sale: Sale) -> Invoice:

        invoice_number = self._generate_invoice_number()
        taxes = sale.taxes
        issued_at = sale.recorded_at

        invoice = Invoice(
            id=None,
            number=invoice_number,
            sale_id=sale.id,
            total_amount=sale.total_amount,
            items=[InvoiceItem(
                product_id=item.product_id,
                product_name=item.product_name,
                quantity=item.quantity,
                unit_price=item.price,
                total_price=self.calculate_product_total_price(item.price, item.quantity)
            ) for item in sale.order.products],
            client_info= None,
            taxes=taxes,
            issued_at=issued_at
        )
        return invoice
    
    def fiscalize_invoice(self, invoice_id:int, client_info: Client_Info) -> Invoice:
        '''this function add client information to an invoice to fiscalize it'''
        invoice = self.get_by_id(invoice_id)
        if not invoice:
            raise ValueError(f"La factura con ID {invoice_id} no existe.")
        if not client_info:
            raise ValueError("La información del cliente es obligatoria para fiscalizar la factura.")
        
        invoice.client_info = client_info

        ### Agregar la funcion de enviar la factura a la persona que provee la informacion
        return invoice
    
    def get_by_id(self, invoice_id:int) -> Invoice:
        db_invoice = self.repository.get_invoice_by_id_with_items(invoice_id)
        if not db_invoice:
            return None
        return Invoice(
            id=db_invoice.id,
            number=db_invoice.number,
            sale_id=db_invoice.sale_id,
            total_amount=db_invoice.total_amount,
            items= [InvoiceItem(
                product_id=item.product_id,
                product_name=item.product_name,
                unit_price=item.unit_price,
                quantity=item.quantity,
                total_price=item.total_price
            ) for item in db_invoice.items],
            client_info=Client_Info(
                id = db_invoice.client_document,
                name = db_invoice.client_name,
                email=db_invoice.client_email,
                doc_type= db_invoice.client_document_type
            ) if db_invoice.client_email else None,
            taxes=db_invoice.taxes,
            issued_at=db_invoice.issued_at
        )

    def save_invoice(self, invoice: Invoice) -> Invoice:
        if invoice.id:
            db_invoice = self.repository.update_invoice(invoice)
        else:
            db_invoice = self.repository.create_invoice(invoice)
        invoice.id = db_invoice.id
        return invoice

    def _delete(self, invoice_id:int):
        '''This function only we use to delovment mode'''
        db_invoice_deleted = self.repository.delete_invoice(invoice_id)
        if not db_invoice_deleted: 
            raise ValueError(f'La factura con id {invoice_id} no existe!')
        return Invoice(

        )
        
    def calculate_product_total_price(self, unit_price: float, quantity: int) -> float:
        return unit_price * quantity
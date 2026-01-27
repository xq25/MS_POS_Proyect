from sqlalchemy.orm import Session, joinedload
from src.domain.models.Invoices import Invoice
from src.infrastructure.db.models.invoiceModel import InvoiceModel
from src.infrastructure.db.models.invoiceItemModel import InvoiceItemModel

class InvoiceRepositorySQLAlchemy:
    def __init__(self, db: Session):
        self.db = db

    def get_invoice_by_id_with_items(self, invoice_id: int)-> InvoiceModel:
        db_invoice = self.db.query(InvoiceModel).options(joinedload(InvoiceModel.items)).filter(InvoiceModel.id == invoice_id).first()
        if not db_invoice:
            return None
        return db_invoice

    def get_invoice_by_number_with_items(self, invoice_number: str)-> InvoiceModel:
        db_invoice = self.db.query(InvoiceModel).options(joinedload(InvoiceModel.items)).filter(InvoiceModel.number == invoice_number).first()
        if not db_invoice:
            return None
        return db_invoice
    
    def get_invoice_by_sale_id_with_items(self, sale_id: int)-> InvoiceModel:
        db_invoice = self.db.query(InvoiceModel).options(joinedload(InvoiceModel.items)).filter(InvoiceModel.sale_id == sale_id).first()
        if not db_invoice:
            return None
        return db_invoice
    
    def create_invoice(self, invoice: Invoice)-> InvoiceModel:
        db_invoice = InvoiceModel(
            number=invoice.number,
            sale_id=invoice.sale_id,
            total_amount=invoice.total_amount,
            taxes=invoice.taxes,
            issued_at=invoice.issued_at,
            client_document=invoice.client_info.id if invoice.client_info else None,
            client_name=invoice.client_info.name if invoice.client_info else None,
            client_email=invoice.client_info.email if invoice.client_info else None,
            client_document_type=invoice.client_info.doc_type if invoice.client_info else None
        )
        self.db.add(db_invoice)
        self.db.flush()
        
        # Agregar items a la factura
        for item in invoice.items:
            db_item = InvoiceItemModel(
                invoice_id=db_invoice.id,
                product_name=item.product_name,
                unit_price=item.unit_price,
                quantity=item.quantity,
                total_price=item.total_price
            )
            self.db.add(db_item)
        
        self.db.flush()
        self.db.refresh(db_invoice)
        return db_invoice

    def update_invoice(self, invoice: Invoice)-> InvoiceModel:
        db_invoice = self.db.query(InvoiceModel).get(invoice.id)

        if not db_invoice:
            return None
        
        # Datos Obligatorios
        db_invoice.total_amount = invoice.total_amount
        db_invoice.issued_at = invoice.issued_at

        # Datos Opcionales Ligados Al Tipo De Facturacion
        db_invoice.client_document = invoice.client_info.id if invoice.client_info else None
        db_invoice.client_name = invoice.client_info.name if invoice.client_info else None
        db_invoice.client_email = invoice.client_info.email if invoice.client_info else None
        db_invoice.client_document_type = invoice.client_info.doc_type if invoice.client_info else None
        
        # Actualizar items
            # Eliminar items antiguos
        self.db.query(InvoiceItemModel).filter(InvoiceItemModel.invoice_id == db_invoice.id).delete()
        
        # Agregar nuevos items
        for item in invoice.items:
            db_item = InvoiceItemModel(
                invoice_id=db_invoice.id,
                product_name=item.product_name,
                unit_price=item.unit_price,
                quantity=item.quantity,
                total_price=item.total_price
            )
            self.db.add(db_item)
        
        self.db.flush()
        self.db.refresh(db_invoice)
        return db_invoice
    
    def delete_invoice(self, invoice_id: int)-> InvoiceModel | None:
        db_invoice = self.db.query(InvoiceModel).get(invoice_id)

        if not db_invoice:
            return None
        self.db.delete(db_invoice)
        self.db.flush()

        return db_invoice
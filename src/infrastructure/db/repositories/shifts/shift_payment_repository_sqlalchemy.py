from datetime import datetime
from sqlalchemy.orm import Session, joinedload
from src.domain.models.Shifts import ShiftPayment
from src.infrastructure.db.models.shiftPaymentModel import ShiftPaymentModel
from src.infrastructure.db.models.shiftModel import ShiftModel

class ShiftPaymentRepositorySQLAlchemy:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[ShiftPaymentModel]:
        db_shiftPs = (self.db.query(ShiftPaymentModel)
                      .options(joinedload(ShiftPaymentModel.shifts)
                              .joinedload(ShiftModel.employee))
                      .all())
        if not db_shiftPs:
            return []
        return db_shiftPs

    def get_by_id(self, shiftPayment_id: int) -> ShiftPaymentModel | None:
        db_shiftP = (self.db.query(ShiftPaymentModel)
                     .options(joinedload(ShiftPaymentModel.shifts)
                             .joinedload(ShiftModel.employee))
                     .filter(ShiftPaymentModel.id == shiftPayment_id)
                     .first())
        if not db_shiftP:
            return None
        return db_shiftP
    
    def get_by_shift_id(self, shift_id: int) -> ShiftPaymentModel | None:
        db_shiftP = (self.db.query(ShiftPaymentModel)
                     .options(joinedload(ShiftPaymentModel.shifts)
                            .joinedload(ShiftModel.employee))
                     .filter(ShiftPaymentModel.shifts.any(id=shift_id))
                     .first())
        if not db_shiftP:
            return None
        return db_shiftP

    def get_by_payment_date(self, start_date:datetime, final_date:datetime)->list[ShiftPaymentModel]:
        db_shifts_payment = (self.db.query(ShiftPaymentModel)
                            .options(joinedload(ShiftPaymentModel.shifts)
                                    .joinedload(ShiftModel.employee))
                            .filter(start_date < ShiftPaymentModel.payment_date, final_date > ShiftPaymentModel.payment_date))
        if not db_shifts_payment:
            return None
        return db_shifts_payment

    def create(self, shiftPayment: ShiftPayment) -> ShiftPaymentModel:
        """Crea un nuevo pago de turno y vincula los shifts existentes.
        Args:
            shiftPayment: Objeto ShiftPayment con shifts y amount calculado
        """
        # Extraer los IDs de los shifts
        shift_ids = [s.id for s in shiftPayment.shifts]
        
        db_shiftPayment = ShiftPaymentModel(total_amount=shiftPayment.total_amount)
        self.db.add(db_shiftPayment)
        self.db.flush()  # Para obtener el ID generado
        self.db.refresh(db_shiftPayment)
        
        # Vincular los shifts existentes al pago
        if shift_ids:
            self.db.query(ShiftModel).filter(ShiftModel.id.in_(shift_ids)).update(
                {ShiftModel.shift_payment_id: db_shiftPayment.id}
            )
            self.db.flush()
            self.db.refresh(db_shiftPayment)
        
        return db_shiftPayment

    def update(self, shiftPayment: ShiftPayment) -> ShiftPaymentModel | None:
        """Actualiza un pago de turno y sus shifts asociados.
        Args:
            shiftPayment: Objeto ShiftPayment con los datos actualizados
        """
        db_shiftP = self.get_by_id(shiftPayment.id)
        if not db_shiftP:
            return None
        
        db_shiftP.amount = shiftPayment.amount
        
        # Extraer los IDs de los shifts nuevos
        shift_ids = [s.id for s in shiftPayment.shifts]
        
        # Limpiar vínculos antiguos (desvincular todos los shifts de este pago)
        self.db.query(ShiftModel).filter(
            ShiftModel.shift_payment_id == db_shiftP.id
        ).update({ShiftModel.shift_payment_id: None})
        
        # Vincular los nuevos shifts
        if shift_ids:
            self.db.query(ShiftModel).filter(ShiftModel.id.in_(shift_ids)).update(
                {ShiftModel.shift_payment_id: db_shiftP.id}
            )
        
        self.db.flush()
        self.db.refresh(db_shiftP)
        return db_shiftP

    def delete(self, shiftPayment_id: int) -> ShiftPaymentModel | None:
        db_shiftP = self.db.query(ShiftPaymentModel).get(shiftPayment_id)
        if not db_shiftP:
            return None
        self.db.delete(db_shiftP)
        self.db.flush()
        return db_shiftP

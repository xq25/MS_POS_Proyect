from datetime import datetime, timedelta
from src.domain.models.Shifts import Shift, ShiftPayment, HourDistribution, Employee
from src.infrastructure.db.models.shiftPaymentModel import ShiftPaymentModel
from src.infrastructure.db.repositories.shifts.shift_payment_repository_sqlalchemy import ShiftPaymentRepositorySQLAlchemy

class ShiftPaymentService:
    def __init__(self, shiftPayRepository: ShiftPaymentRepositorySQLAlchemy):
        self.repository = shiftPayRepository
    
    def db_to_domain(self, db_model:ShiftPaymentModel) -> ShiftPayment:
        return ShiftPayment(
            id=db_model.id,
            shifts=[Shift(id = s.id,
                          employee = Employee(
                              id = s.employee_id,
                              name = s.employee.name,
                              email = s.employee.email,
                              phone = s.employee.phone,
                              roles = [],
                              salary = s.employee.salary
                          ),
                          start_at = s.start_at,
                          end_at = s.end_at,
                          total_hours = s.total_hours,
                          is_active = s.is_active,
                          shift_payment_id = s.shift_payment_id
                        )for s in db_model.shifts],
            payment_date = db_model.payment_date,
            amount = db_model.total_amount
        )
    
    def get_by_id(self, shift_payment_id:int) -> ShiftPayment:
        db_shift_payment = self.repository.get_by_id(shift_payment_id)
        if not db_shift_payment:
            raise ValueError(f'El pago de turnos con id {shift_payment_id} no ha sido encontrado')
        return self.db_to_domain(db_shift_payment)

    def get_by_shift_id(self, shift_id) -> ShiftPayment:
        db_shift_payment = self.repository.get_by_shift_id(shift_id)
        if not db_shift_payment:
            raise ValueError(f'El pago de turnos con id {shift_id} no ha sido encontrado')
        return self.db_to_domain(db_shift_payment)
    
    def get_by_payment_date(self, paymentdate:datetime) -> list[ShiftPayment]:
        '''PaymentDate -> tiene que ser la referencia de el inicio de un dia, a las 00 horas para poder manetener una buena logica'''
        if paymentdate.minute > 0 or paymentdate.hour > 0 or paymentdate.second > 0 :
            paymentdate.replace(hour=0,minute=0,second=0, microsecond=0)
        if paymentdate > datetime.utcnow():
            raise ValueError(f'Las consultas de pagos por fechas no pueden superar la fecha actual {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")}')
        
        start_date = paymentdate
        final_date = paymentdate + timedelta(days=1)
        db_shifts = self.repository.get_by_payment_date(start_date, final_date)

        if not db_shifts:
            return []
        
        return [self.db_to_domain(db_sp) for db_sp in db_shifts]
    
    def create(self, shiftList: list[Shift]) -> ShiftPayment:
        # Validaciones previas a la creacion | Validations prior to creating
        self.validations(shiftList)

        unique_employee = shiftList[0].employee
        total_hour_distibution = self.calculate_total_hourDistribution(shiftList)
        sp = ShiftPayment(
            id=None,
            shifts=shiftList,
            payment_date=datetime.utcnow(),
        )
        sp.amount = sp.calculate_total_amount(unique_employee.salary, [total_hour_distibution])

        db_shiftP = self.repository.create(sp)
        return self.db_to_domain(db_shiftP)

    def update(self, shiftPayment: ShiftPayment) -> ShiftPayment:
        # Validaciones previas a la actualizacion | Validations prior to updating
        self.validations(shiftPayment.shifts)

        # Actualizacion del total_amount por defecto
        total_hours_distribution = self.calculate_total_hourDistribution(shiftPayment.shifts)
        shiftPayment.total_amount = shiftPayment.calculate_total_amount(shiftPayment.shifts[0].employee.salary, [total_hours_distribution])
        
        db_shift_payment = self.repository.update(shiftPayment)

        if not db_shift_payment:
            raise ValueError(f'El pago de turnos con id {shiftPayment.id} no ha sido encontrado')
        
        return self.db_to_domain(db_shift_payment)
    
    def delete(self, shift_payment_id:int) -> ShiftPayment:
        db_shift_payment_deleted = self.repository.delete(shift_payment_id)

        if not db_shift_payment_deleted:
            raise ValueError(f'El pago de turnos con id {shift_payment_id} no ha sido encontrado')
        
        return self.db_to_domain(db_shift_payment_deleted)
    
    # Metodos informativos y validaciones | Validations and Informative Methods
    def calculate_total_hourDistribution(self, shiftList:list[Shift]) -> HourDistribution:
        total_hd = HourDistribution()

        if len(shiftList)> 1:
            for i in shiftList:
                iteratorHd = i.hoursDistribution(i.start_at, i.end_at, i.total_hours)
                total_hd.daytime_hours += iteratorHd.daytime_hours
                total_hd.night_hours += iteratorHd.night_hours
                total_hd.overtime_hours += iteratorHd.overtime_hours
                total_hd.sunday_holyday_hours += iteratorHd.sunday_holyday_hours
        else:
            uniqueShift = shiftList[0]
            total_hd = uniqueShift.hoursDistribution(uniqueShift.start_at, uniqueShift.end_at, uniqueShift.total_hours)

        return total_hd
    
    def unique_employee_validation(self, shiftList:list[Shift]) -> None:
        unique_employee = shiftList[0].employee.id

        if len(shiftList)>1:
            for sf in shiftList:
                if sf.employee.id != unique_employee:
                    raise ValueError(f'La lista de turnos a pagar debe pertenecer a un unico empleado | Unique_Employee_ID: {unique_employee} != {sf.employee.id}')
        return 
    
    def max_min_len_shiftList_validation(self, shiftList:list[Shift]) -> None:
        if len(shiftList) > 15 or len(shiftList) <1:
            raise ValueError('La generacion de pagos solo puede albergar maximo 15 turnos y minimo 1 turno')
        return 
    
    def validations(self, shiftList:list[Shift]) -> None:
        try:
            self.unique_employee_validation(shiftList)
            self.max_min_len_shiftList_validation(shiftList)
        except ValueError as e:
            raise ValueError(f'Error en la validacion de turnos a pagar: {e}')
            
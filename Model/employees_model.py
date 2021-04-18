from sqlalchemy.orm import sessionmaker
from Domain.employees import Employees
from View.utils import engine


class EmployeesModel:
    def __init__(self):
        self.__engine = engine
        self.__my_session = sessionmaker(bind=engine)()

    def create_employee(self, employee_id, first_name, last_name, job):
        self.__my_session.add(
            Employees(
                employee_id=employee_id,
                first_name=first_name,
                last_name=last_name,
                job=job
            )
        )
        self.__my_session.commit()

    def read_employee(self):
        self.__my_session.query(Employees).all()

    def update_employee(self, employee_id, first_name, last_name, job):
        my_employee = self.__my_session.query(Employees).filter_by(employee_id=employee_id).first()
        if my_employee:
            self.__my_session.query(
                Employees
            ).filter_by(
                employee_id
            ).update({
                'first_name': f'{first_name or my_employee.first_name}',
                'last_name': f'{last_name or my_employee.last_name}',
                'job': f'{job or my_employee.job}'

            })
        self.__my_session.commit()

    def delete_employee(self, employee_id):
        self.__my_session.query(Employees).filter_by(employee_id=employee_id).delete()
        self.__my_session.commit()

    def find_by_id(self, employee_id):
        my_employee = self.__my_session.query(Employees).filter_by(employee_id=employee_id).first()
        return my_employee

    def id_exists(self, employee_id):
        my_employee = self.__my_session.query(Employees).filter_by(employee_id=employee_id).first()
        return True if my_employee else False

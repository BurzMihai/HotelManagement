from sqlalchemy import Column, Integer, String
from View.utils import Base


class Employees(Base):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    job = Column(String, nullable=False)

    def __str__(self):
        return (f'employee_id: {self.employee_id}\n'
                f'first_name: {self.first_name}\n'
                f'last_name: {self.last_name}\n'
                f'job: {self.job}')

    def __repr__(self):
        return (f'employee_id: {self.employee_id}\n'
                f'first_name: {self.first_name}\n'
                f'last_name: {self.last_name}\n'
                f'job: {self.job}')

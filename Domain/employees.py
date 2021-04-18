from sqlalchemy import Column, Integer, String
from View.utils import Base


class Employees(Base):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    job = Column(String, nullable=False)

    def __repr__(self):
        return f'{self.employee_id, self.first_name, self.last_name, self.job}'

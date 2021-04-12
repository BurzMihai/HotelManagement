from View.utils import Base
from sqlalchemy import Column, Integer


class Reservation(Base):
    __tablename__ = 'reservations'
    reservations_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, nullable=False)
    room_number = Column(Integer, nullable=False)
    start_date = Column(Integer, nullable=False)
    end_date = Column(Integer, nullable=False)

    def __repr__(self):
        return f' {self.reservations_id}, {self.client_id}, {self.room_number}'

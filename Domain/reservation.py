from Domain.client import Client
from Domain.room import Room
from View.utils import Base
from sqlalchemy import Column, Integer, Date, ForeignKey


class Reservation(Base):
    __tablename__ = 'reservations'
    reservations_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey(Client.client_id), nullable=False)
    room_number = Column(Integer, ForeignKey(Room.room_number), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    def __repr__(self):
        return f' {self.reservations_id}, {self.client_id}, {self.room_number}'

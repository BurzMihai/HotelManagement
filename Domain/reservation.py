from sqlalchemy.sql.functions import current_date

from Domain.client import Client
from Domain.room import Room
from View.utils import Base
from sqlalchemy import Column, Integer, Date, ForeignKey


class Reservation(Base):
    __tablename__ = 'reservations'
    reservations_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey(Client.client_id), nullable=False)
    room_number = Column(Integer, ForeignKey(Room.room_number), nullable=False)
    start_date = Column(Date, nullable=False, default=current_date())
    end_date = Column(Date, nullable=False)

    def __str__(self):
        return (f'reservation_id: {self.reservations_id}\n'
                f'client_id: {self.client_id}\n'
                f'room_number: {self.room_number}\n'
                f'start_date: {self.start_date}\n'
                f'end_date: {self.end_date}')

    def __repr__(self):
        return (f'reservation_id: {self.reservations_id}\n'
                f'client_id: {self.client_id}\n'
                f'room_number: {self.room_number}\n'
                f'start_date: {self.start_date}\n'
                f'end_date: {self.end_date}')

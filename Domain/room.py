from View.utils import Base
from sqlalchemy import Column, Integer, String, Float, Boolean


class Room(Base):
    __tablename__ = 'room'
    room_number = Column(Integer, primary_key=True)
    room_type = Column(String, nullable=False)
    price_per_night = Column(Float, nullable=False)
    size = Column(Integer, nullable=False)
    has_view = Column(Boolean, nullable=False)

    def __str__(self):
        return (f'room_number: {self.room_number}\n'
                f'room_type: {self.room_type}\n'
                f'price_per_night: {self.price_per_night}\n'
                f'size: {self.size}\n'
                f'has_view: {self.has_view}')

    def __repr__(self):
        return (f'room_number: {self.room_number}\n'
                f'room_type: {self.room_type}\n'
                f'price_per_night: {self.price_per_night}\n'
                f'size: {self.size}\n'
                f'has_view: {self.has_view}')

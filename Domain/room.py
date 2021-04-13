from View.utils import Base
from sqlalchemy import Column, Integer, String, Float, Boolean


class Room(Base):
    __tablename__ = 'room'
    room_number = Column(Integer, primary_key=True)
    room_type = Column(String, nullable=False)
    price_per_night = Column(Float, nullable=False)
    size = Column(Integer, nullable=False)
    has_view = Column(Boolean, nullable=False)

    def __repr__(self):
        return f' {self.room_number}, {self.room_type}, {self.price_per_night}, {self.size}'

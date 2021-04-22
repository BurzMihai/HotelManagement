from sqlalchemy import Column, Integer, String, create_engine

from Model.room_model import RoomModel
from View.utils import Base


class Client(Base):
    __tablename__ = 'clients'
    client_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __str__(self):
        return (f'client_id: {self.client_id}\n'
                f'first_name: {self.first_name}\n'
                f'last_name: {self.last_name},\n'
                f'email: {self.email}')

    def __repr__(self):
        return (f'client_id: {self.client_id}\n'
                f'first_name: {self.first_name}\n'
                f'last_name: {self.last_name},\n'
                f'email: {self.email}')

    def return_client_as_dict(self):
        return {'client_id': self.client_id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email}



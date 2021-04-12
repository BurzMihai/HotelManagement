from sqlalchemy import Column, Integer, String

from View.utils import Base


class Client(Base):
    __tablename__ = 'clients'
    client_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        return f' {self.client_id}, {self.first_name}, {self.last_name}, {self.email}'

from sqlalchemy.orm import sessionmaker
from Domain.client import Client
from View.utils import engine


class ClientsModel:
    def __init__(self, engine):
        self.__engine = engine
        self.__my_session = sessionmaker(bind=engine)()

    def read_client(self):
        return self.__my_session.query(Client).all()

    def create_client(self, client_id, first_name, last_name, email):
        self.__my_session.add(
            Client(
                client_id=client_id,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
        )
        self.__my_session.commit()

    def update_client(self, client_id, first_name, last_name, email):
        my_client = self.__my_session.query(Client).filter_by(client_id=client_id).first()
        if my_client:
            self.__my_session.query(
                Client
            ).filter_by(
                client_id=client_id
            ).update({
                'firstname': f'{first_name or my_client.first_name}',
                'lastname': f'{last_name or my_client.last_name}',
                'email': f'{email or my_client.email}'
            })
            self.__my_session.commit()

    def delete_client(self, client_id):
        self.__my_session.query(Client).filter_by(client_id=client_id).delete()
        self.__my_session.commit()

    def find_by_id(self, client_id):
        my_client = self.__my_session.query(Client).filter_by(client_id=client_id).first()
        return my_client

    def id_exists(self, client_id):
        my_client = self.__my_session.query(Client).filter_by(client_id=client_id).first()
        return True if my_client else False



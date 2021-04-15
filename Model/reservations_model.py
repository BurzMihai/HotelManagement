from sqlalchemy.orm import sessionmaker

from Domain.reservation import Reservation
from View.utils import engine


class ClientsModel:
    def __init__(self):
        self.__my_session = sessionmaker(bind=engine)()
        self.__engine = engine

    def read_room(self):
        self.__my_session.query(Reservation).all()

    def create_reservation(self, reservations_id, client_id, room_number, start_date, end_date):
        self.__my_session.add(
            Reservation(
                reservations_id=reservations_id,
                client_id=client_id,
                room_number=room_number,
                start_date=start_date,
                end_date=end_date
            )
        )
        self.__my_session.commit()

    def update_reservation(self, reservations_id, start_date, end_date):
        my_reservation = self.__my_session.query(Reservation).filter_by(reservations_id=reservations_id).first()
        if my_reservation:
            self.__my_session.query(
                Reservation
            ).filter_by(
                reservations_id=reservations_id
            ).update({
                'start_date': f'{start_date or my_reservation.start_date}',
                'end_date': f'{end_date or my_reservation.end_date}',
            })
            self.__my_session.commit()

    def delete_reservation(self, reservations_id):
        self.__my_session.query(Reservation).filter_by(reservations_id=reservations_id).delete()
        self.__my_session.commit()

    def find_by_reservation_id(self, reservations_id):
        my_reservation = self.__my_session.query(Reservation).filter_by(reservations_id=reservations_id).first()
        return my_reservation

    def reservation_exists(self, reservations_id):
        my_reservation = self.__my_session.query(Reservation).filter_by(reservations_id=reservations_id).first()
        return True if my_reservation else False

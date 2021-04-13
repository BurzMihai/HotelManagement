from sqlalchemy.orm import sessionmaker
from Domain.room import Room
from View.utils import engine


class RoomModel:
    def __init__(self):
        self.__my_session = sessionmaker(bind=engine)()
        self.__engine = engine

    def read_room(self):
        self.__my_session.query(Room).all()

    def create_room(self, room_number, room_type, price_per_night, size, has_view):
        self.__my_session.add(
            Room(
                room_number=room_number,
                room_type=room_type,
                price_per_night=price_per_night,
                size=size,
                has_view=has_view
            )
        )
        self.__my_session.commit()

    def update_room(self, room_number, room_type, price_per_night, size, has_view):
        my_room = self.__my_session.query(Room).filter_by(room_number=room_number).first()
        if my_room:
            self.__my_session.query(
                Room
            ).filter_by(
                room_number=room_number
            ).update({
                'room_type': f'{room_type or my_room.room_type}',
                'price_per_night': f'{price_per_night or my_room.price_per_night}',
                'size': f'{size or my_room.size}',
                'has_view': f'{has_view or my_room.has_view}'
            })
            self.__my_session.commit()

    def delete_room(self, room_number):
        self.__my_session.query(Room).filter_by(room_number=room_number).delete()
        self.__my_session.commit()

    def find_by_room_number(self, room_number):
        my_room = self.__my_session.query(Room).filter_by(room_number=room_number).first()
        return my_room

    def room_exists(self, room_number):
        my_room = self.__my_session.query(Room).filter_by(room_number=room_number).first()
        return True if my_room else False

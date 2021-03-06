from flask import Flask, request
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine

from Domain import client
from Model import client_model, reservations_model
from Model.client_model import ClientsModel
from Model.reservations_model import ReservationsModel
from Model.room_model import RoomModel

app = Flask('my_hotel_api')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/get_all_clients')
@cross_origin()
def get_all_clients():
    client_list = client_model.read_client()
    clients_as_dict = []
    for client in client_list:
        clients_as_dict.append(client.return_client_as_dict())
    client_json = {
        'clients': clients_as_dict
    }
    return client_json


@app.route('/add_client', methods=['POST'])
@cross_origin()
def add_client():
    data = request.get_json()
    print(data)
    client_model.create_client(
        client_id=data['client_id'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
    )

    return "200"


@app.route('/add_reservation', methods=['POST'])
@cross_origin()
def add_client():
    data = request.get_json()
    print(data)
    reservations_model.create_reservation(
        reservations_id=data['reservations_id'],
        client_id=data['client_id'],
        room_number=data['room_number'],
        start_date=data['start_date'],
        end_date=data['end_date']
    )

    return "200"


@app.route('/top5reviews')
@cross_origin()
def top5reviews():
    pass


if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:@127.0.0.1:3305/hotel', echo=False)
    client_model = ClientsModel(engine=engine)
    room_model = RoomModel(engine=engine)
    reservations_model = ReservationsModel(engine=engine)
    app.run(debug=True)

from flask import Flask, request
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine

from Domain import client
from Model import client_model
from Model.client_model import ClientsModel
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


if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:@127.0.0.1:3305/hotel', echo=False)
    client_model = ClientsModel(engine=engine)
    room_model = RoomModel(engine=engine)
    app.run(debug=True)

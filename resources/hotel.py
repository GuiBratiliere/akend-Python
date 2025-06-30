from flask_restful import Resource, reqparse
from Models.hotel import HotelModel

hoteis = [
    {
        "id": 1,
        "nome": "Hotel Mar Azul",
        "cidade": "Rio de Janeiro",
        "preco": 320.00,
        "estrelas": 4,
        "disponivel": True
    },
    {
        "id": 2,
        "nome": "Pousada das Montanhas",
        "cidade": "Campos do Jordão",
        "preco": 280.00,
        "estrelas": 3,
        "disponivel": True
    },
    {
        "id": 3,
        "nome": "Hotel Central Palace",
        "cidade": "São Paulo",
        "preco": 450.00,
        "estrelas": 5,
        "disponivel": False
    },
    {
        "id": 4,
        "nome": "Resort do Sol",
        "cidade": "Fortaleza",
        "preco": 520.00,
        "estrelas": 5,
        "disponivel": True
    },
    {
        "id": 5,
        "nome": "Hotel Econômico Express",
        "cidade": "Curitiba",
        "preco": 180.00,
        "estrelas": 2,
        "disponivel": True
    },
    {
        "id": 6,
        "nome": "Pousada Beira-Mar",
        "cidade": "Salvador",
        "preco": 230.00,
        "estrelas": 3,
        "disponivel": False
    },
    {
        "id": 7,
        "nome": "Hotel Luxo Premium",
        "cidade": "Brasília",
        "preco": 620.00,
        "estrelas": 5,
        "disponivel": True
    },
    {
        "id": 8,
        "nome": "Pousada Natureza Viva",
        "cidade": "Bonito",
        "preco": 350.00,
        "estrelas": 4,
        "disponivel": True
    },
    {
        "id": 9,
        "nome": "Hotel Centro Histórico",
        "cidade": "Ouro Preto",
        "preco": 260.00,
        "estrelas": 3,
        "disponivel": True
    },
    {
        "id": 10,
        "nome": "Resort das Águas",
        "cidade": "Foz do Iguaçu",
        "preco": 490.00,
        "estrelas": 4,
        "disponivel": False
    }
]

class Hoteis(Resource):
    def get(self):
        return {'Hoteis': hoteis}
    
class Hotel(Resource):

    #define o contrutor só é chamado quando solicitado no parse_args
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('cidade')
    argumentos.add_argument('preco')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('disponivel')

    def verifica_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['id'] == hotel_id:
                return hotel
        return None 
    
    def get(self, hotel_id):
        hotel = Hotel.verifica_hotel(hotel_id)
        if hotel:
            return hotel
        return { 'message': 'Hotel not found!' }, 404


    def post(self, hotel_id):
        
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.jason()

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.jason()

        hotel = Hotel.verifica_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        global hoteis
        hoteis = [ hotel for hotel in hoteis if hotel['id'] != hotel_id]
        return {'message':'hotel deletado'}
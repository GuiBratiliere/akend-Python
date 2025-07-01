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
        return {'Hoteis': [hotel.json() for hotel in HotelModel.query.all()]}
    
class Hotel(Resource):

    #define o contrutor só é chamado quando solicitado no parse_args
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="O campo 'nome' não pode ficar em branco")
    argumentos.add_argument('cidade', type=str)
    argumentos.add_argument('preco', type=float, required=True)
    argumentos.add_argument('estrelas', type=float)
    argumentos.add_argument('disponivel', type=str)
    
    def get(self, hotel_id):
        hotel = HotelModel.verifica_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return { 'message': 'Hotel not found!' }, 404


    def post(self, hotel_id):
        if HotelModel.verifica_hotel(hotel_id):
            return {'message': 'Hotel já existe!'}, 400
        
        
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'Houve um erro interno ao salvar'}, 500
        return hotel.json()

    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()
        
        hotel_encontrado = HotelModel.verifica_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'Houve um erro interno ao salvar'}, 500
        return hotel.json(), 201

    def delete(self, hotel_id):
        hotel = HotelModel.verifica_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'Houve um erro interno ao salvar'}, 500
            return {'message':'hotel deletado'}
        return {'message': 'Hotel não existe!'}, 404
from SQL_Alchemy import banco


class  HotelModel(banco.Model):
    __tablename__ = 'hoteis'

    hotel_id = banco.Column(banco.String, primary_key = True)
    nome = banco.Column(banco.String(80))
    cidade = banco.Column(banco.String(80))
    preco = banco.Column(banco.Float(precision=2))
    estrelas = banco.Column(banco.Float(precision=1))
    disponivel = banco.Column(banco.String)

    def __init__(self, hotel_id, nome, cidade, preco, estrelas, disponivel):
        self.hotel_id = hotel_id
        self.nome = nome
        self.cidade = cidade 
        self.preco = preco
        self.estrelas = estrelas
        self.disponivel = disponivel
    def json(self):
        return{
        "id": self.hotel_id,
        "nome": self.nome,
        "cidade": self.cidade,
        "preco": self.preco,
        "estrelas": self.estrelas,
        "disponivel": self.disponivel
        }
    
    @classmethod
    def verifica_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()
        if hotel:
            return hotel
        return None
    
    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()

    def update_hotel(self, nome, cidade, preco, estrelas, disponivel):
        self.nome = nome
        self.cidade = cidade 
        self.preco = preco
        self.estrelas = estrelas
        self.disponivel = disponivel

    def delete_hotel(self):
        banco.session.delete(self)
        banco.session.commit()
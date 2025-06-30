

class  HotelModel:
    def __init__(self, hotel_id, nome, cidade, preco, estrelas, disponivel):
        self.hotel_id = hotel_id
        self.nome = nome
        self.cidade = cidade 
        self.preco = preco
        self.estrelas = estrelas
        self.disponivel = disponivel
    def jason(self):
        return{
        "id": self.hotel_id,
        "nome": self.nome,
        "cidade": self.cidade,
        "preco": self.preco,
        "estrelas": self.estrelas,
        "disponivel": self.disponivel
        }
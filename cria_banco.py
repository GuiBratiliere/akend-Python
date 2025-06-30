import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis ( id number PRIMARY KEY,\
      nome text, cidade test, preco real, estrelas real, disponivel boolean)"

cria_hotel = "INSERT INTO hoteis VALUES(1,'Hotel Mar Azul','Rio de Janeiro',320.00,4,True)"

cursor.execute(cria_tabela)
cursor.execute(cria_hotel)

connection.commit()
connection.close()

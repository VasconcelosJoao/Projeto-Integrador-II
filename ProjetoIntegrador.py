import requests
import psycopg2
from psycopg2 import sql

# Fazendo a requisição
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?idLegislatura=56&ordenarPor=nome'
response = requests.get(url)
data = response.json()

# Conectando ao banco de dados
conn = psycopg2.connect(
    dbname="pi2",
    user="postgres",
    password="2605",
    host="localhost",
    port="5432"
)

# Criando a tabela
cur = conn.cursor()
table_create_query = """
CREATE TABLE IF NOT EXISTS deputados (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    partido VARCHAR(50)
)
"""
cur.execute(table_create_query)
conn.commit()

# Inserindo os dados na tabela
for deputado in data['dados']:
    insert_query = sql.SQL("""
        INSERT INTO deputados (id, nome, partido) 
        VALUES (%s, %s, %s)
    """)
    cur.execute(insert_query, (deputado['id'], deputado['nome'], deputado['siglaPartido']))

conn.commit()
cur.close()
conn.close()
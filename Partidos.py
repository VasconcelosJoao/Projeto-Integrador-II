import requests
import psycopg2

# Fazendo a requisição

url = 'https://dadosabertos.camara.leg.br/api/v2/partidos'

params = {'idLegislatura':'56','ordenarPor':'sigla', 'itens': 100}


try:
    response = requests.get(url,params=params)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Erro ao fazer a requisição: {e}")
    exit()

data = response.json()

# Conectando ao banco de dados
try:
    with psycopg2.connect(
        dbname="pi2",
        user="postgres",
        password="2605",
        host="localhost",
        port="5432"
    ) as conn:
        with conn.cursor() as cur:
            # Criando a tabela
            table_create_query = """
            CREATE TABLE IF NOT EXISTS partidos (
                sigla VARCHAR(50) PRIMARY KEY,
                nome VARCHAR(255)
            )
            """
            cur.execute(table_create_query)

            # Inserindo os dados na tabela
            for partido in data['dados']:
                insert_query = """
                INSERT INTO partidos (sigla, nome) 
                VALUES (%s, %s)
                """
                cur.execute(insert_query, (partido['sigla'], partido['nome']))
            conn.commit()
except psycopg2.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    exit()
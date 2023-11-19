import requests
import psycopg2
from psycopg2 import sql
from datetime import datetime

# Conectando ao banco de dados
conn = psycopg2.connect(
    dbname="pi2",
    user="postgres",
    password="2605",
    host="localhost",
    port="5432"
)

# Criando um novo cursor
cur = conn.cursor()

# Criando a tabela gastos se ela não existir
cur.execute("""
    CREATE TABLE IF NOT EXISTS gastos (
        id SERIAL PRIMARY KEY,
        id_deputado INTEGER REFERENCES deputados(id),
        data DATE,
        valor FLOAT,
        tipoDespesa VARCHAR(255),
        codDocumento INTEGER,
        partido VARCHAR(50)
    )
""")
conn.commit()  # Confirmar a transação após a criação da tabela

# Selecionando todos os IDs de deputados e seus partidos
cur.execute("SELECT id, partido FROM deputados")
deputados = cur.fetchall()
count = 0
# Para cada deputado
for deputado in deputados:
    id_deputado = deputado[0]
    partido = deputado[1]  # Buscando o partido do deputado
    pagina = 1
    count += 1
    print(count)
    while True:
        # Fazendo a requisição para a API
        url = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{id_deputado}/despesas'
        params = {'ano':'2020', 'pagina': pagina, 'itens': 100, 'ordenarPor':'dataDocumento'}
        response = requests.get(url, params=params)
        data = response.json()

        # Se não houver mais dados, sair do loop
        if not data['dados']:
            break

        # Para cada gasto do deputado
        for gasto in data['dados']:
            # Se gasto['dataDocumento'] não for None, converter para um objeto datetime
            # if gasto['dataDocumento'] is not None:
            #     data_gasto = datetime.strptime(gasto['dataDocumento'], '%Y-%m-%d')

            #     # Se o ano do gasto for 2020, inserir o gasto na tabela gastos
            #     if data_gasto.year == 2020:
            cur.execute("""
                INSERT INTO gastos (id_deputado, data, valor, tipoDespesa, codDocumento, partido) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (id_deputado, gasto['dataDocumento'], gasto['valorLiquido'], gasto['tipoDespesa'], gasto['codDocumento'], partido))
            conn.commit()  # Confirmar a transação após cada inserção

        # Ir para a próxima página
        pagina += 1
# Fechando o cursor e a conexão
cur.close()
conn.close()
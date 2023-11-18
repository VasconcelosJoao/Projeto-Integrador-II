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
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS gastos_estranhos (
        id SERIAL PRIMARY KEY,
        id_deputado INTEGER,
        data DATE,
        valor FLOAT,
        tipoDespesa VARCHAR(255),
        codDocumento INTEGER
    )
""")
conn.commit()

# Encontrando as linhas com valores estranhos
cur.execute("""
    SELECT * FROM gastos WHERE TO_CHAR(data, 'YYYY') != '2020' OR codDocumento = 0
""")
rows = cur.fetchall()

# Inserindo as linhas estranhas na nova tabela e removendo da tabela original
for row in rows:
    cur.execute("""
        INSERT INTO gastos_estranhos (id_deputado, data, valor, tipoDespesa, codDocumento) 
        VALUES (%s, %s, %s, %s, %s)
    """, (row[1], row[2], row[3], row[4], row[5]))
    cur.execute("""
        DELETE FROM gastos WHERE id = %s
    """, (row[0],))
    conn.commit()

# Fechando o cursor e a conexão
cur.close()
conn.close()
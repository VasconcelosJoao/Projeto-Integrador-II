import requests
import psycopg2

# Conectando ao banco de dados
with psycopg2.connect(
    dbname="pi2",
    user="postgres",
    password="2605",
    host="localhost",
    port="5432"
)as conn:
    with conn.cursor() as cur: 
        # Criando a tabela gastos se ela não existir

        cur.execute("""
            CREATE TABLE IF NOT EXISTS gastos_estranhos (
                id SERIAL PRIMARY KEY,
                id_deputado INTEGER REFERENCES deputados(id),
                data DATE,
                valor FLOAT,
                tipoDespesa VARCHAR(255),
                codDocumento INTEGER,
                partido VARCHAR(50) REFERENCES partidos(sigla)
            )
        """)
        conn.commit()

        # Encontrando as linhas com valores estranhos
        cur.execute("""
            SELECT * FROM gastos WHERE TO_CHAR(data, 'YYYY') != '2020' OR codDocumento = 0 OR valor <= 0
        """)
        rows = cur.fetchall()

        # Inserindo as linhas estranhas na nova tabela e removendo da tabela original
        for row in rows:
            cur.execute("""
                INSERT INTO gastos_estranhos (id_deputado, data, valor, tipoDespesa, codDocumento, partido) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (row[1], row[2], row[3], row[4], row[5], row[6]))
            cur.execute("""
                DELETE FROM gastos WHERE id = %s
            """, (row[0],))
            conn.commit()

        # Fechando o cursor e a conexão
    cur.close()
    conn.close()
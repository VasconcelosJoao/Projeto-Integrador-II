# Projeto Integrador 2

## Descrição

Este projeto visa analisar os gastos públicos da Câmara dos Deputados do Brasil durante o ano de 2020. O objetivo é coletar dados através da API da Câmara, armazená-los em um banco de dados relacional, e realizar análises utilizando técnicas de Business Intelligence e Machine Learning para identificar padrões e irregularidades nos gastos dos deputados.

## Tabela de Conteúdos

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Banco de Dados](#estrutura-do-banco-de-dados)
- [Análises Realizadas](#análises-realizadas)
- [Considerações Finais](#considerações-finais)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Tecnologias Utilizadas

- Python
- PostgreSQL
- Pandas
- Scikit-learn
- Power BI

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seuusuario/projeto-integrador-2.git
   cd projeto-integrador-2
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure o banco de dados**:
   - Crie um banco de dados PostgreSQL chamado `pi2`.
   - Atualize as credenciais de conexão no script conforme necessário.

## Uso

Para executar o projeto, utilize o script principal que faz a coleta de dados e a análise:

```bash
python main.py
```

## Estrutura do Banco de Dados

O banco de dados é composto pelas seguintes tabelas:

- **partidos**: Armazena informações sobre os partidos.
  - `sigla`: VARCHAR(50) (Chave Primária)
  - `nome`: VARCHAR(255)

- **deputados**: Armazena informações sobre os deputados.
  - `id`: SERIAL (Chave Primária)
  - `nome`: VARCHAR(255)
  - `partido`: VARCHAR(50) (Chave Estrangeira)

- **gastos**: Armazena os gastos dos deputados.
  - `id`: SERIAL (Chave Primária)
  - `id_deputado`: INTEGER (Chave Estrangeira)
  - `data`: DATE
  - `valor`: FLOAT
  - `tipoDespesa`: VARCHAR(255)
  - `codDocumento`: INTEGER
  - `partido`: VARCHAR(50) (Chave Estrangeira)

## Análises Realizadas

### Análise de Gastos

- Identificação dos deputados que mais gastaram em 2020.
- Análise dos principais tipos de despesas.
- Detecção de gastos suspeitos.

### Machine Learning

- Utilização de algoritmos de regressão para identificar fatores que influenciam os gastos dos deputados.
- Geração de previsões sobre gastos futuros com base nos dados históricos.

## Considerações Finais

O projeto proporcionou uma visão detalhada sobre os gastos públicos, permitindo a identificação de padrões e possíveis irregularidades. Durante o desenvolvimento, foram enfrentados desafios relacionados à coleta e manipulação de dados, mas as soluções encontradas foram eficazes.

## Contribuição

Contribuições são bem-vindas! Para contribuir, siga os passos abaixo:

1. Fork o repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça suas alterações e commit (`git commit -m 'Adicionando nova funcionalidade'`).
4. Envie para o repositório remoto (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

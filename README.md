# Data Analytics

Projeto prático de Big Data e Analytics que integra coleta, processamento, armazenamento, Machine Learning e visualização de dados.

## Objetivo

Construir um pipeline de dados capaz de processar avaliações de produtos, analisar sentimentos e disponibilizar indicadores para análise em um dashboard.

## Arquitetura

```text
Producer
   |
   v
Apache Kafka
   |
   v
Consumer + Análise de Sentimentos
   |
   v
MongoDB
   |
   v
Python ETL
   |
   v
CSV
   |
   v
Power BI
```

O Apache Airflow é utilizado para orquestrar a execução do processo ETL.

## Tecnologias

- **Python:** processamento e transformação de dados.
- **Apache Kafka:** transmissão de mensagens.
- **Machine Learning:** classificação de sentimentos com TF-IDF e Regressão Logística.
- **MongoDB:** armazenamento dos dados processados.
- **Apache Airflow:** agendamento e orquestração do ETL.
- **Pandas:** manipulação e exportação dos dados.
- **Power BI:** criação de dashboards e indicadores.
- **Git e GitHub:** versionamento e documentação do projeto.
- **Docker:** execução do ambiente do Airflow.

## Dashboard

O dashboard desenvolvido no Power BI apresenta indicadores como:

- Total de avaliações.
- Nota média.
- Distribuição de sentimentos.
- Avaliações por categoria.
- Nota média por categoria.
- Filtros por categoria, nota e sentimento.

Arquivo: `DataAnalytics_Dashboard.pbix`.

## Estrutura do projeto

```text
DataAnalytics/
├── src/
│   ├── kafka_producer.py
│   ├── kafka_consumer.py
│   ├── sentiment_analysis.py
│   ├── sentiment_model.py
│   └── mongo_to_csv.py
├── data/
│   ├── models/
│   └── processed/
│       └── reviews_analytics.csv
├── airflow/
│   ├── dags/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── docker-compose.yaml
├── docs/
│   ├── architecture.md
│   └── project_overview.md
├── DataAnalytics_Dashboard.pbix
└── README.md
```

## Execução do ETL

Com o MongoDB em execução e as dependências instaladas, execute na raiz do projeto:

```bash
python src/mongo_to_csv.py
```

O script extrai os documentos da coleção `reviews_processed`, transforma os dados e gera o arquivo:

`data/processed/reviews_analytics.csv`

Para utilizar o Airflow, inicie o ambiente Docker na pasta `airflow`:

```bash
docker compose up -d --build
```

A interface do Airflow fica disponível em `http://localhost:8080`.

## Limitações conhecidas

- A qualidade da classificação de sentimentos ainda pode ser aprimorada.
- O dashboard depende da atualização dos dados de origem e da atualização do arquivo utilizado pelo Power BI.
- O acesso ao MongoDB e os caminhos dos arquivos devem estar configurados corretamente no ambiente de execução.

## Status

Projeto desenvolvido para demonstrar conceitos e ferramentas de Big Data, ETL, Machine Learning, orquestração de dados e Business Intelligence.

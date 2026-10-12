# Arquitetura do Pipeline de Big Data

## Visão geral

O projeto implementa um pipeline de processamento de avaliações de clientes, integrando ingestão de eventos, processamento de texto, armazenamento NoSQL, ETL, orquestração e visualização analítica.

## Arquitetura

1. **Kafka Producer:** envia avaliações para o sistema de mensageria.
2. **Apache Kafka:** transporta os eventos entre produtor e consumidor.
3. **Kafka Consumer:** recebe e encaminha os dados para processamento.
4. **NLP e Machine Learning:** utiliza TF-IDF e Logistic Regression para classificação de sentimentos.
5. **MongoDB:** armazena os registros processados na base `data_analytics`, coleção `reviews_processed`.
6. **Python ETL:** consulta o MongoDB, converte os campos necessários e exporta `data/processed/reviews_analytics.csv`.
7. **Apache Airflow:** agenda e orquestra a execução do ETL por meio da DAG `etl_reviews_mongodb_csv`.
8. **Power BI:** utiliza o CSV para construir indicadores, gráficos e filtros interativos.

## Tecnologias

- Python e Pandas
- Apache Kafka 4.3.1 com KRaft
- TF-IDF e Logistic Regression
- MongoDB e PyMongo
- Apache Airflow 3.3.1
- Docker Compose
- Power BI
- Git e GitHub

## Organização

- `src/`: produtor, consumidor, classificação de sentimentos e ETL.
- `data/models/`: modelos treinados localmente.
- `data/processed/`: dados analíticos exportados.
- `airflow/dags/`: definições dos fluxos de orquestração.
- `docs/`: documentação do projeto.
- `notebooks/`: espaço para análises exploratórias.
- `DataAnalytics_Dashboard.pbix`: dashboard do Power BI.

## Execução do ETL

O ambiente do Airflow utiliza Docker Compose. O serviço MongoDB precisa estar acessível pelo container.

Na pasta `airflow`, execute:

```powershell
docker compose up -d
```

A interface do Airflow fica disponível em `http://localhost:8080`.

A DAG `etl_reviews_mongodb_csv` executa `src/mongo_to_csv.py`, que gera o CSV utilizado pelo Power BI. A programação definida é diária, às 08h de Brasília, considerando a configuração UTC do Airflow.

Para encerrar o ambiente:

```powershell
docker compose down
```

O comando acima não remove o volume persistente do Airflow.

## Configuração e segurança

O endereço do MongoDB é configurado pela variável `MONGODB_URI`. O script Python utiliza `mongodb://localhost:27017/` como padrão local, enquanto o Docker Compose utiliza `mongodb://host.docker.internal:27017/` para acessar o MongoDB executado no Windows.

Credenciais, tokens e arquivos de ambiente com segredos não devem ser versionados. Modelos treinados e arquivos temporários devem permanecer fora do controle de versão quando não forem necessários para a reprodução do projeto.

## Considerações

O pipeline integra os componentes principais de engenharia de dados e análise. A qualidade das classificações depende do modelo treinado e dos dados utilizados. Antes de aplicações reais, recomenda-se validar o desempenho do classificador, a integridade dos dados e o tratamento de falhas.

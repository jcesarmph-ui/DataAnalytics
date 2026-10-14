# Data Analytics | Engenharia de Dados, Big Data e Machine Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white" alt="Apache Kafka"/>
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB"/>
  <img src="https://img.shields.io/badge/Apache_Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white" alt="Apache Airflow"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-learn"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
</p>

<p align="center">
  Pipeline de dados para processamento de avaliações de produtos, classificação de sentimentos, armazenamento de informações e construção de indicadores analíticos.
</p>

---

## Visão Geral

O Data Analytics é um projeto de Engenharia de Dados e Ciência de Dados que integra diferentes etapas de um fluxo analítico, desde a geração e o processamento de informações até a disponibilização de indicadores em um dashboard.

O projeto utiliza avaliações de produtos como fonte de dados para demonstrar a integração entre mensageria, processamento em Python, armazenamento NoSQL, orquestração de tarefas e Business Intelligence.

A solução combina processamento de dados e Machine Learning para transformar avaliações textuais em informações estruturadas que podem ser exploradas por meio de indicadores e filtros.

## Objetivos

- Estruturar um pipeline de processamento de dados.
- Demonstrar a transmissão de mensagens com Apache Kafka.
- Aplicar técnicas de Processamento de Linguagem Natural à análise de sentimentos.
- Armazenar os dados processados no MongoDB.
- Automatizar a execução do fluxo ETL com Apache Airflow.
- Preparar conjuntos de dados para análise e visualização.
- Desenvolver um dashboard analítico no Power BI.

## Arquitetura do Pipeline

O fluxo integra componentes de mensageria, processamento, armazenamento, transformação e visualização.

```text
┌───────────────────────────────────┐
│      Geração de avaliações        │
│             Python                │
└─────────────────┬─────────────────┘
                  │
                  ▼
┌───────────────────────────────────┐
│           Apache Kafka            │
│      Transmissão de mensagens      │
└─────────────────┬─────────────────┘
                  │
                  ▼
┌───────────────────────────────────┐
│      Consumer e análise de        │
│      sentimentos com Python       │
└─────────────────┬─────────────────┘
                  │
                  ▼
┌───────────────────────────────────┐
│             MongoDB               │
│    Armazenamento dos resultados   │
└─────────────────┬─────────────────┘
                  │
                  ▼
┌───────────────────────────────────┐
│          Processo ETL             │
│  Extração, transformação e carga  │
└─────────────────┬─────────────────┘
                  │
                  ▼
┌───────────────────────────────────┐
│               CSV                 │
│       Dados preparados            │
└─────────────────┬─────────────────┘
                  │
                  ▼
┌───────────────────────────────────┐
│             Power BI              │
│       Dashboard analítico         │
└───────────────────────────────────┘

Apache Airflow: orquestração do processo ETL.
Docker: execução do ambiente de orquestração.
```

## Etapas de Processamento

### 1. Geração e transmissão de dados

O produtor gera mensagens de avaliações e utiliza o Apache Kafka para transmitir os dados ao consumidor.

### 2. Processamento e análise de sentimentos

Os dados textuais são processados para identificar sentimentos associados às avaliações.

A abordagem de Machine Learning utiliza:

- TF-IDF para representação numérica do texto.
- Regressão Logística para classificação.
- Pré-processamento das avaliações.
- Geração de resultados estruturados para as etapas seguintes.

### 3. Armazenamento NoSQL

O MongoDB armazena os documentos processados, permitindo organizar os resultados da análise e disponibilizá-los para extração posterior.

### 4. Extração, transformação e carga

Um processo ETL implementado em Python realiza a extração dos documentos armazenados, organiza os campos relevantes e exporta os dados para um arquivo CSV.

O Apache Airflow é utilizado para orquestrar a execução do processo, enquanto o Docker auxilia na configuração do ambiente de execução.

### 5. Visualização e análise

Os dados preparados são utilizados pelo Power BI para construir um dashboard com indicadores e filtros analíticos.

## Dashboard Analítico

O arquivo `DataAnalytics_Dashboard.pbix` contém o dashboard desenvolvido para exploração dos resultados.

### Indicadores disponíveis

- Total de avaliações.
- Nota média.
- Distribuição dos sentimentos classificados.
- Quantidade de avaliações por categoria.
- Nota média por categoria.
- Filtros por categoria, nota e sentimento.

O dashboard permite explorar a distribuição das avaliações e comparar os resultados entre diferentes categorias de produtos.

## Tecnologias e Ferramentas

| Tecnologia | Aplicação |
|---|---|
| Python | Geração, processamento e transformação dos dados. |
| Apache Kafka | Transmissão de mensagens entre produtor e consumidor. |
| Scikit-learn | Implementação do classificador de sentimentos. |
| TF-IDF | Representação vetorial dos textos. |
| Regressão Logística | Classificação de sentimentos. |
| MongoDB | Armazenamento dos documentos processados. |
| Pandas | Manipulação e exportação de dados tabulares. |
| Apache Airflow | Orquestração do processo ETL. |
| Docker | Execução do ambiente do Airflow. |
| Power BI | Construção do dashboard e dos indicadores. |
| CSV | Intercâmbio de dados entre o ETL e a ferramenta de visualização. |
| Git e GitHub | Versionamento e documentação do projeto. |

## Estrutura do Repositório

```text
DataAnalytics/
├── airflow/
│   ├── dags/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── docker-compose.yaml
├── data/
│   ├── models/
│   └── processed/
│       └── reviews_analytics.csv
├── docs/
│   ├── architecture.md
│   └── project_overview.md
├── src/
│   ├── kafka_producer.py
│   ├── kafka_consumer.py
│   ├── sentiment_analysis.py
│   ├── sentiment_model.py
│   └── mongo_to_csv.py
├── DataAnalytics_Dashboard.pbix
└── README.md
```

## Competências Demonstradas

- Engenharia de Dados e integração de componentes.
- Processamento de dados e construção de pipelines ETL.
- Mensageria e processamento de eventos.
- Bancos de dados NoSQL.
- Processamento de Linguagem Natural.
- Machine Learning aplicado à classificação de textos.
- Orquestração de tarefas.
- Containerização de ambientes.
- Business Intelligence e visualização de indicadores.

---

**Projeto de integração entre Engenharia de Dados, Machine Learning e Business Intelligence, com foco na transformação de avaliações textuais em informações estruturadas para análise.**

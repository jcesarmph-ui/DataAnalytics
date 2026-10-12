# Visão Geral do Projeto

## Objetivo

Desenvolver um projeto prático de Big Data e Analytics capaz de processar avaliações de clientes, armazenar os resultados e disponibilizar informações para análise.

## Problema abordado

Avaliações de clientes contêm informações estruturadas, como notas e categorias, e informações textuais, como comentários. O projeto reúne essas informações em um fluxo de processamento para facilitar a análise de sentimentos e o acompanhamento de indicadores.

## Solução implementada

O pipeline integra:

- Ingestão de dados com Apache Kafka.
- Processamento de comentários com NLP e Machine Learning.
- Persistência em MongoDB.
- Transformação e exportação de dados com Python e Pandas.
- Orquestração do ETL com Apache Airflow.
- Visualização de indicadores no Power BI.

## Principais resultados

O projeto possui componentes para ingestão, processamento, armazenamento, transformação, orquestração e visualização. A DAG `etl_reviews_mongodb_csv` foi executada com sucesso no ambiente local, gerando o arquivo CSV utilizado pelo dashboard.

## Indicadores do dashboard

- Total de avaliações.
- Nota média.
- Percentuais por sentimento.
- Distribuição de sentimentos.
- Avaliações por categoria.
- Nota média por categoria.
- Filtros interativos para exploração dos dados.

## Tecnologias

Python, Pandas, Apache Kafka, MongoDB, PyMongo, TF-IDF, Logistic Regression, Apache Airflow, Docker Compose, Power BI e GitHub.

## Situação do projeto

A implementação local dos principais componentes está concluída em sua versão inicial. A qualidade do classificador, o monitoramento, os testes automatizados e a evolução da infraestrutura podem ser aprimorados futuramente, conforme a necessidade.

## Repositório

Código-fonte e documentação: https://github.com/jcesarmph-ui/DataAnalytics

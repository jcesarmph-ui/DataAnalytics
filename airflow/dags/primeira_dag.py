
from datetime import datetime

from airflow.sdk import dag, task


@dag(
    dag_id="primeira_dag_big_data",
    description="Primeiro fluxo de teste do projeto Data Analytics",
    schedule=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["big-data", "teste"],
)
def primeira_dag_big_data():

    @task
    def verificar_pipeline():
        print("Airflow funcionando!")
        print("Primeira DAG do projeto Data Analytics executada com sucesso.")

    verificar_pipeline()


primeira_dag_big_data()

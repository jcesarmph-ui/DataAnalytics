
from datetime import datetime

from airflow.sdk import dag, task


@dag(
    dag_id="etl_reviews_mongodb_csv",
    description="Extrai avaliações do MongoDB e gera o CSV para o Power BI",
    schedule=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["big-data", "etl", "mongodb", "power-bi"],
)
def etl_reviews_mongodb_csv():

    @task
    def executar_etl():
        import subprocess

        resultado = subprocess.run(
            [
                "python",
                "/opt/project/src/mongo_to_csv.py",
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        print(resultado.stdout)

        if resultado.stderr:
            print(resultado.stderr)

    executar_etl()


etl_reviews_mongodb_csv()

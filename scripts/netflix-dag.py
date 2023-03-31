
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'gomes',
    'depends_on_past': False,
    "start_date": datetime(2022, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    "netflix-pipeline",
    default_args=default_args,
    description="A simple pipeline DAG",
    schedule_interval=timedelta(days=1),
    catchup=False,
)   

t1  = BashOperator(
    task_id="netflix-api",
    bash_command="source /Users/gomes/.pyenv/versions/project6/bin/activate && python /Users/gomes/Desktop/Projects/Data\ Engineer/6-Project/scripts/netflix-api.py",
    dag=dag,
)

t2  = BashOperator(
    task_id="data-process",
    bash_command="source /Users/gomes/.pyenv/versions/project6/bin/activate && python /Users/gomes/Desktop/Projects/Data\ Engineer/6-Project/scripts/data-process.py",
    dag=dag,
)

t3  = BashOperator(
    task_id="process-data",
    bash_command="source /Users/gomes/.pyenv/versions/project6/bin/activate && python /Users/gomes/Desktop/Projects/Data\ Engineer/6-Project/scripts/bigquery.py",
    dag=dag,
)

t4 = BashOperator(
    task_id='dbt_run',
    bash_command="source /Users/gomes/.pyenv/versions/project6/bin/activate && cd /Users/gomes/Desktop/Projects/Data\ Engineer/6-Project/wu5project && dbt run",
    dag=dag,
)

t1 >> t2 >> t3 >> t4


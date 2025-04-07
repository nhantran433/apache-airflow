from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'nhan',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),

}

with DAG(
    default_args=default_args,
    dag_id = 'dag_with_cron_expression_v01',
    start_date=datetime(2025, 3, 4),
    schedule_interval='5 4 * * *', # at 04:05 daily, access crontab.guru to get the rule 
    catchup=True
) as dag:
    task1=BashOperator(
        task_id = 'greet',
        bash_command='echo dag with cron expression!'
    )

    task1
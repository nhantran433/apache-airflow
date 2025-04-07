from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'nhan',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='my_first_dag_v3',
    default_args=default_args,
    description='This is my first dag that I write',
    start_date=datetime(2025, 3, 4, 2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task!"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo this is task2, will be running after task1"
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo this is task3, will be running after task1 and running at the same time with task2"
    )

    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # task1 >> task2
    # task1 >> task3

    [task2, task3] >> task1
    task1 >> [task2, task3]
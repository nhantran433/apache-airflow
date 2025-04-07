from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'nhan',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet():
    print("Hello World!")

def greet_v2(name, age):
    print(f"My name is {name}, and I am {age} years old!")

def greet_v3(age, ti):
    name = ti.xcom_pull(task_ids='get_name')
    print(f"My name is {name}, and I am {age} years old!")

def greet_v4(age, ti):
    firstname = ti.xcom_pull(task_ids='get_name_v2', key='first_name')
    lastname = ti.xcom_pull(task_ids='get_name_v2', key='last_name')
    print(f"My name is {firstname} {lastname}, and I am {age} years old!")

def get_name():
    return "Tom"

def get_name_v2(ti):
    ti.xcom_push(key='first_name', value='Jerry')
    ti.xcom_push(key='last_name', value='Fridman')


with DAG(
    default_args=default_args,
    dag_id = 'dag_with_python_operator_python_v05',
    description="My dag using python operator",
    start_date=datetime(2025, 3, 4),
    schedule_interval='@daily'
) as dag:
    # task1=PythonOperator(
    #     task_id = 'greet',
    #     python_callable=greet
    # )

    # task2=PythonOperator(
    #     task_id = 'greet_v2',
    #     python_callable=greet,
    #     op_kwargs={'name': 'Tom', 'age': 20}
    # )

    # task4=PythonOperator(
    #     task_id = 'greet_v3',
    #     python_callable=greet_v3,
    #     op_kwargs={'age': 20}
    # )

    task6=PythonOperator(
        task_id = 'greet_v4',
        python_callable=greet_v4,
        op_kwargs={'age': 20}
    )

    # task3=PythonOperator(
    #     task_id='get_name',
    #     python_callable=get_name
    # )

    task5=PythonOperator(
        task_id='get_name_v2',
        python_callable=get_name_v2
    )
    
    # task1 >> task2
    task5 >> task6

    #Kich thuoc toi da cua xcom la 48kb :v
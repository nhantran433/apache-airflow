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
    dag_id = 'dag_with_catchup_and_backfill_v01',
    start_date=datetime(2025, 3, 4),
    schedule_interval='@daily',
    catchup=True
) as dag:
    task1=BashOperator(
        task_id = 'greet',
        bash_command='echo This is a simple bash command!'
    )

    task1

# catchup=True: Airflow sẽ tự động chạy lại các task cho các ngày đã bị bỏ lỡ từ start_date đến ngày hiện tại.
# catchup=False: Airflow chỉ chạy task cho ngày hiện tại và bỏ qua các task đã bị bỏ lỡ trước đó.
# Backfill trong Apache Airflow là quá trình tự động chạy các task đã bị bỏ lỡ trong quá khứ, đặc biệt là khi bạn đã bật tính năng catchup=True cho một DAG.
# Khi một DAG có catchup=True (mặc định), Airflow sẽ thực hiện backfilling các task cho các ngày trước đó nếu DAG chưa chạy hoặc nếu các task không được thực thi vào những ngày đó vì lý do nào đó (chẳng hạn như hệ thống không hoạt động hoặc DAG mới được kích hoạt sau khi đã có một số ngày trôi qua).

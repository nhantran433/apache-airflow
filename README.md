## Run Apache Airflow with Docker

### Step 1: Open Bash or WSL in your working directory
To download the `docker-compose.yaml` file, run the following command:

```bash
curl -Lf0 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
```

### Step 2: Create directories for DAGs, Plugins, and Logs
```bash
mkdir ./dags ./plugins ./logs 
```

### Step 3: Initialize Airflow
```bash
docker-compose up airflow-init
```

### Step 4: Start Airflow
```bash
docker-compose
```

### Step 5: Access Airflow

Access Airflow at `localhost:8080/admin`.

Login with:

- **User**: airflow
- **Password**: airflow
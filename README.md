# Data-Engineer - Netflix - Study Case

## Netflix

For Netflix, understanding user interactions and preferences is crucial for providing personalized content, recommendations, and improving customer retention. In this project, i will build a streaming data pipeline using Google Cloud Platform (GCP) to ingest, process, and store user interaction data in real-time.

### Data Pipeline Steps

1. **Infrastructure**: Provision necessary GCP resources using Terraform.
2. **CI/CD**: Use GitHub Actions as a CI/CD platform for the Terraform infrastructure.
3. **Data Modeling**: Develop a Python script using the Faker library to simulate user interaction data, such as watch history, ratings, and session duration. Additionally, include user demographic information and subscription details.
4. **Data Ingestion**: Ingest the generated data into the GCP ecosystem using Pub/Sub for real-time event streaming.
5. **Data Processing**: Use DataFlow to process and enrich the ingested data. This may involve calculating aggregate metrics like average session duration, number of movies watched per week, and content preferences.
6. **Data Lake Process Storage**: Store the processed data in GCP Cloud Storage for further analysis or use in other projects.
7. **Data Warehouse**: Load the processed data into GCP BigQuery for storage and analysis..
8. **Data Transformation**: Use DBT to transform and clean the data in BigQuery, making it suitable for reporting and analytics purposes.
9. **Data Orchestration**:  Set up GCP Composer and configure an Apache Airflow environment.

### Pipeline Diagram

![alt text](https://github.com/makima0499/6.Data-Engineer/blob/main/6.DataPipeline.png)

### Tools

* Python
* Jupyter
* Terraform
* Github Actions
* GCP PubSub
* GCP Dataflow
* GCP Storage
* GCP BigQuery
* GCP Composer(Airflow)
* DBT

### Note

This repository is provided for study purposes only, focusing on data engineering pipelines.

## License

[MIT](https://choosealicense.com/licenses/mit/)

from google.cloud import bigquery
from google.oauth2 import service_account

# Set Google Cloud project ID and dataset ID
project_id = 'wu6project'
dataset_id = 'wu6datasetid'

# Set the path to service account key file
service_account_key_file = '../service-account/wu6project-3e0f2c673612.json'

# Load service account credentials
credentials = service_account.Credentials.from_service_account_file(service_account_key_file)

# Initialize the BigQuery client
client = bigquery.Client(project=project_id, credentials=credentials)

# Set the table ID
table_id = f"{project_id}.{dataset_id}.netflix_table"

# Set the URI of GCS data
uri = "gs://wu6process/output/output-*"

# Create a LoadJobConfig
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    schema=[
        bigquery.SchemaField("user_id", "STRING"),
        bigquery.SchemaField("content_id", "STRING"),
        bigquery.SchemaField("content_title", "STRING"),
        bigquery.SchemaField("content_category", "STRING"),
        bigquery.SchemaField("genre", "STRING"),
        bigquery.SchemaField("watch_date", "DATE"),
        bigquery.SchemaField("rating", "INTEGER"),
        bigquery.SchemaField("session_duration", "INTEGER"),
    ],
    write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
)

# Create a table reference
table_ref = client.dataset(dataset_id).table("netflix_table")

# Run the LoadJob
load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)

# Wait for the job to complete
load_job.result()

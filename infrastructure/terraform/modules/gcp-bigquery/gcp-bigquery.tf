resource "google_bigquery_dataset" "default" {
  dataset_id                  = "wu6datasetid"
  friendly_name               = "wu6bigquery"
  description                 = "This is a bigquery for netflix project"
  location                    = "US"

  labels = {
    env = "default"
  }
  access {
    role          = "OWNER"
    user_by_email = google_service_account.bqowner.email
  }

  access {
    role   = "READER"
    domain = "hashicorp.com"
  }
}

resource "google_service_account" "bqowner" {
  account_id = "wu6bqowner"
}
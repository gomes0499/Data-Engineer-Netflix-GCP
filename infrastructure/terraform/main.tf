module "gcp_pubsub" {
    source = "./modules/gcp-pubsub"
}

module "gcp_storage" {
    source = "./modules/gcp-storage"
}

module "gcp_bigquery" {
    source = "./modules/gcp-bigquery"
}

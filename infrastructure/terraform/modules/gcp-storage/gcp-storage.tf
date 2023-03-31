resource "google_storage_bucket" "processed_data_bucket" {
  name          = "wu6process"
  location      = "US"
  force_destroy = true

  uniform_bucket_level_access = true
}


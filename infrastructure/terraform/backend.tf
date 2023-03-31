terraform {
  backend "gcs" {
    bucket  = "wu6tfstate"
    prefix  = "terraform/state"
  }
}

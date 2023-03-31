resource "google_pubsub_topic" "example" {
  name = "wu6topic"

  labels = {
    foo = "bar"
  }

  message_retention_duration = "86600s"
}

resource "google_pubsub_subscription" "example_subscription" {
  name  = "wu6sub"
  topic = google_pubsub_topic.example.name

  ack_deadline_seconds = 20
}


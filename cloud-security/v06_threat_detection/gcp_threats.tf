# Illustrative, not run here: check the current docs
resource "google_pubsub_topic" "scc_threats" {
  name    = "scc-threats"
  project = "my-project"
}
resource "google_scc_notification_config" "threats" {
  config_id    = "high-threats"
  organization = "123456789"
  description  = "Threat findings, high or critical"
  pubsub_topic = google_pubsub_topic.scc_threats.id
  streaming_config {
    filter = "finding_class = \"THREAT\" AND severity = \"HIGH\""
  }
}

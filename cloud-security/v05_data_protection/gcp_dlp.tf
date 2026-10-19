# Illustrative, not run here: check the current docs
resource "google_data_loss_prevention_inspect_template" "india_pii" {
  parent       = "projects/my-project/locations/global"
  display_name = "India PII and cards"
  inspect_config {
    min_likelihood = "LIKELY"
    info_types { name = "INDIA_AADHAAR_INDIVIDUAL" }
    info_types { name = "INDIA_PAN_INDIVIDUAL" }
    info_types { name = "CREDIT_CARD_NUMBER" }
  }
}
# a discovery scan profiles every bucket with this template

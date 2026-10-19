# Illustrative, not run here: check the current docs
# Stop anyone creating downloadable service account keys
gcloud resource-manager org-policies enable-enforce \
  iam.disableServiceAccountKeyCreation \
  --organization=123456789012

# Find the user-managed keys that already exist
gcloud iam service-accounts keys list \
  --iam-account=reports-bot@my-project.iam.gserviceaccount.com \
  --managed-by=user

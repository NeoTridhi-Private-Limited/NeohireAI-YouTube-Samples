# Illustrative, not run here: check the current docs
# Retention policy: objects cannot be deleted for 30 days
gcloud storage buckets update gs://hospital-backups \
  --retention-period=30d
# Lock it. A locked policy can never be removed or shortened
gcloud storage buckets update gs://hospital-backups \
  --lock-retention-period
gcloud storage buckets describe gs://hospital-backups

# Illustrative, not run here: check the current docs
# MRI bucket: block public access, one permission model
gcloud storage buckets update gs://my-project-mri-scans \
  --public-access-prevention \
  --uniform-bucket-level-access

gcloud storage buckets describe gs://my-project-mri-scans

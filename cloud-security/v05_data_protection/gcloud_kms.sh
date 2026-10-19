# Illustrative, not run here: check the current docs
gcloud kms keyrings create hospital-ring --location=asia-south1
gcloud kms keys create reports-key --keyring=hospital-ring \
  --location=asia-south1 --purpose=encryption \
  --rotation-period=90d --next-rotation-time=2026-12-01T00:00:00Z
RING=projects/my-project/locations/asia-south1/keyRings/hospital-ring
# allow the Cloud Storage service agent to use the key
gcloud storage service-agent --project=my-project \
  --authorize-cmek=$RING/cryptoKeys/reports-key
gcloud storage buckets update gs://hospital-reports \
  --default-encryption-key=$RING/cryptoKeys/reports-key
gcloud storage buckets update gs://hospital-reports \
  --public-access-prevention

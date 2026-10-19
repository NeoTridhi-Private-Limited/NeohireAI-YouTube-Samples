# Illustrative, not run here: check the current docs
# Scan images in Artifact Registry, and enforce the policy on GKE
gcloud services enable \
  containerscanning.googleapis.com \
  binaryauthorization.googleapis.com
gcloud container binauthz policy import binauthz_policy.yaml
gcloud container clusters update shop-cluster \
  --region=asia-south1 \
  --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE

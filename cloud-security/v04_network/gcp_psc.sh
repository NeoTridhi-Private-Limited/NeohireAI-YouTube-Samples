# Illustrative, not run here: check the current docs
# Reach Google APIs through a private IP inside the VPC
gcloud compute addresses create psc-apis-ip --global \
  --purpose=PRIVATE_SERVICE_CONNECT --addresses=10.10.0.5 \
  --network=portal-vpc
# Endpoint name: lowercase letters and digits, up to 20 characters
gcloud compute forwarding-rules create pscapis --global \
  --network=portal-vpc --address=psc-apis-ip \
  --target-google-apis-bundle=all-apis

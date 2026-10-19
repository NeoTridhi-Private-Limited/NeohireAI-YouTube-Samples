# Illustrative, not run here: check the current docs
# Web servers take HTTPS only from Google's load balancer ranges
gcloud compute firewall-rules create allow-lb-https \
  --network=shop-vpc --direction=INGRESS --action=ALLOW \
  --rules=tcp:443 --target-tags=web --priority=1000 \
  --source-ranges=130.211.0.0/22,35.191.0.0/16
# The database takes MySQL only from the web tier's service account
gcloud compute firewall-rules create allow-web-to-db \
  --network=shop-vpc --direction=INGRESS --action=ALLOW \
  --rules=tcp:3306 \
  --source-service-accounts=web@my-project.iam.gserviceaccount.com \
  --target-service-accounts=db@my-project.iam.gserviceaccount.com
# Admins use IAP for SSH instead of a public port 22
gcloud compute firewall-rules create allow-iap-ssh \
  --network=shop-vpc --direction=INGRESS --action=ALLOW \
  --rules=tcp:22 --source-ranges=35.235.240.0/20

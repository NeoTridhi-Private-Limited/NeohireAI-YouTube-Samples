# Illustrative, not run here: check the current docs
gcloud compute security-policies create shop-armor \
  --description="Diwali sale protection"
# Block SQL injection with a preconfigured WAF rule
gcloud compute security-policies rules create 1000 \
  --security-policy=shop-armor --action=deny-403 \
  --expression="evaluatePreconfiguredWaf('sqli-v422-stable')"
# Throttle any IP above 100 login requests a minute
gcloud compute security-policies rules create 2000 \
  --security-policy=shop-armor --action=throttle \
  --expression="request.path.matches('/login')" \
  --rate-limit-threshold-count=100 \
  --rate-limit-threshold-interval-sec=60 \
  --conform-action=allow --exceed-action=deny-429 --enforce-on-key=ip
gcloud compute backend-services update shop-backend --global \
  --security-policy=shop-armor

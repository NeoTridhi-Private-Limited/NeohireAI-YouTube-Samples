# Illustrative, not run here: check the current docs
# Put Identity-Aware Proxy in front of the reports app's backend
gcloud compute backend-services update reports-backend \
  --global --iap=enabled
# Only doctors, and only from a laptop that meets the access level
cat > cond.yaml <<'EOF'
title: corp-laptops-only
expression: >-
  "accessPolicies/<policy-id>/accessLevels/corp_laptops"
  in request.auth.access_levels
EOF
gcloud iap web add-iam-policy-binding \
  --resource-type=backend-services --service=reports-backend \
  --member=group:doctors@example.com \
  --role=roles/iap.httpsResourceAccessor \
  --condition-from-file=cond.yaml

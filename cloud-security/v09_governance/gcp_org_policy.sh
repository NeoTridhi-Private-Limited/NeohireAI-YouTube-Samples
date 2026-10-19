# Illustrative, not run here: check the current docs
cat > public.yaml <<'EOF'
name: organizations/123456789012/policies/storage.publicAccessPrevention
spec:
  rules:
  - enforce: true
EOF
cat > regions.yaml <<'EOF'
name: organizations/123456789012/policies/gcp.resourceLocations
spec:
  rules:
  - values:
      allowedValues:
      - in:asia-south1-locations
      - in:asia-south2-locations
EOF
gcloud org-policies set-policy public.yaml
gcloud org-policies set-policy regions.yaml

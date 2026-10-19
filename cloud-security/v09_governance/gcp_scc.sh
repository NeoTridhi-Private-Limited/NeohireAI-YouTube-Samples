# Illustrative, not run here: check the current docs
# Detective view: active public bucket findings in Security Command Center
gcloud scc findings list organizations/123456789012 \
  --location=global \
  --filter='state="ACTIVE" AND category="PUBLIC_BUCKET_ACL"' \
  --format="table(finding.resourceName, finding.category)"

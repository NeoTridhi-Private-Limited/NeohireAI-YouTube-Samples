# Illustrative, not run here: check the current docs
# Security Command Center is activated for the organisation in the console
gcloud scc findings list 123456789 --location=global \
  --filter='state="ACTIVE" AND finding_class="MISCONFIGURATION"'
gcloud scc findings list projects/my-gov-portal \
  --filter='state="ACTIVE" AND category="PUBLIC_BUCKET_ACL"'
gcloud scc findings list projects/my-gov-portal \
  --filter='state="ACTIVE" AND category="OPEN_SSH_PORT"'

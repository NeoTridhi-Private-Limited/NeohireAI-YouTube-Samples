# Illustrative, not run here: check the current docs
# Send every audit log in the organisation to one BigQuery dataset
gcloud logging sinks create org-audit-sink \
  bigquery.googleapis.com/projects/my-project/datasets/audit_logs \
  --organization=<org-id> \
  --include-children \
  --log-filter='logName:"cloudaudit.googleapis.com"'

# Illustrative, not run here: check the current docs
# One trail for every account and every region, tamper-evident
aws cloudtrail create-trail \
  --name org-trail \
  --s3-bucket-name my-audit-bucket \
  --is-multi-region-trail \
  --is-organization-trail \
  --enable-log-file-validation \
  --kms-key-id alias/audit-logs
aws cloudtrail start-logging --name org-trail

# Illustrative, not run here: check the current docs
# Threat detection and posture checks, in each region you use
aws guardduty create-detector --enable --region ap-south-1

aws securityhub enable-security-hub --enable-default-standards \
  --region ap-south-1

aws securityhub get-findings --region ap-south-1 --max-items 3 \
  --filters '{"SeverityLabel":[{"Value":"HIGH","Comparison":"EQUALS"}]}'

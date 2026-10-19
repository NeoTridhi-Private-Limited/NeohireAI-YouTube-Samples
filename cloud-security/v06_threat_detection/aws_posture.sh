# Illustrative, not run here: check the current docs
aws securityhub enable-security-hub --enable-default-standards
aws securityhub get-findings --max-items 5 --filters '{
  "ComplianceStatus":[{"Value":"FAILED","Comparison":"EQUALS"}],
  "SeverityLabel":[{"Value":"CRITICAL","Comparison":"EQUALS"}],
  "RecordState":[{"Value":"ACTIVE","Comparison":"EQUALS"}]}' \
  --query 'Findings[].Title'

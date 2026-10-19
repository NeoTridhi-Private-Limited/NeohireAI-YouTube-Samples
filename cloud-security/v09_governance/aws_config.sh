# Illustrative, not run here: check the current docs
# Detective rule: flag any S3 bucket that allows public read
cat > rule.json <<'EOF'
{
  "ConfigRuleName": "no-public-read-buckets",
  "Scope": {"ComplianceResourceTypes": ["AWS::S3::Bucket"]},
  "Source": {"Owner": "AWS",
             "SourceIdentifier": "S3_BUCKET_PUBLIC_READ_PROHIBITED"}
}
EOF
aws configservice put-config-rule --config-rule file://rule.json
aws configservice get-compliance-details-by-config-rule \
  --config-rule-name no-public-read-buckets \
  --compliance-types NON_COMPLIANT

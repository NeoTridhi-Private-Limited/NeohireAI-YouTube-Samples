# Illustrative, not run here: check the current docs
# Turn on the CIS AWS Foundations Benchmark checks in Security Hub
ARN="arn:aws:securityhub:ap-south-1::standards/"
ARN+="cis-aws-foundations-benchmark/v/5.0.0"
aws securityhub batch-enable-standards \
  --standards-subscription-requests StandardsArn=$ARN
aws securityhub get-enabled-standards \
  --query "StandardsSubscriptions[].StandardsStatus"

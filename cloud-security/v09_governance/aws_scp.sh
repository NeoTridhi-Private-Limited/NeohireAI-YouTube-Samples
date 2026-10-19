# Illustrative, not run here: check the current docs
# SCP: deny all outside Mumbai and Hyderabad, except global services
cat > india-only.json <<'EOF'
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Deny", "Resource": "*",
    "NotAction": ["iam:*", "organizations:*", "sts:*", "support:*"],
    "Condition": {"StringNotEquals":
      {"aws:RequestedRegion": ["ap-south-1", "ap-south-2"]}}
  }]
}
EOF
aws organizations create-policy --name india-only \
  --type SERVICE_CONTROL_POLICY --description "India regions only" \
  --content file://india-only.json
aws organizations attach-policy \
  --policy-id p-examplepolicy1 --target-id ou-ab12-prod1234

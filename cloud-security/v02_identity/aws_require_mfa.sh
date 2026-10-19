# Illustrative, not run here: check the current docs
cat > require-mfa.json <<'EOF'
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "DenyMostWithoutMFA", "Effect": "Deny",
    "NotAction": ["iam:ChangePassword", "iam:CreateVirtualMFADevice",
                  "iam:EnableMFADevice", "iam:ListMFADevices",
                  "sts:GetSessionToken"],
    "Resource": "*",
    "Condition": {"BoolIfExists":
                  {"aws:MultiFactorAuthPresent": "false"}}
  }]
}
EOF
aws iam create-policy --policy-name RequireMFA \
  --policy-document file://require-mfa.json

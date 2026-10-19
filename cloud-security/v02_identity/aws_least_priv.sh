# Illustrative, not run here: check the current docs
cat > reports-read.json <<'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {"Sid": "ReadReports", "Effect": "Allow",
     "Action": ["s3:GetObject", "s3:ListBucket"],
     "Resource": ["arn:aws:s3:::my-bank-reports",
                  "arn:aws:s3:::my-bank-reports/*"]},
    {"Sid": "NoSalaryFiles", "Effect": "Deny", "Action": "s3:*",
     "Resource": "arn:aws:s3:::my-bank-reports/salaries/*"}
  ]
}
EOF
aws iam create-policy --policy-name ReportsReadOnly \
  --policy-document file://reports-read.json

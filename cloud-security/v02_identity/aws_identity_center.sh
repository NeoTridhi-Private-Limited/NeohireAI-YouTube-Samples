# Illustrative, not run here: check the current docs
# People sign in through IAM Identity Center: short-lived keys
aws configure sso
#   SSO session name: bank
#   SSO start URL: https://my-bank.awsapps.com/start
#   SSO region: ap-south-1
#   then pick the account and the ReportsReadOnly permission set

aws sso login --profile reports-readonly
aws sts get-caller-identity --profile reports-readonly

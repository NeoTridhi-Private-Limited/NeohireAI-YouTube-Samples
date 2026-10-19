# Illustrative, not run here: check the current docs
# A key leaked to a public repo: switch it off, then clean up
KEY="<leaked-access-key-id>"
aws iam list-access-keys --user-name intern-reports

aws iam update-access-key --user-name intern-reports \
  --access-key-id "$KEY" --status Inactive

# What did the key do while it was out? Ask CloudTrail
aws cloudtrail lookup-events --max-results 20 \
  --lookup-attributes AttributeKey=AccessKeyId,AttributeValue="$KEY"

aws iam delete-access-key --user-name intern-reports \
  --access-key-id "$KEY"

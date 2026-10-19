# Illustrative, not run here: check the current docs
KEY=AKIAIOSFODNN7EXAMPLE
# 1 Contain: switch the leaked key off (it can be switched back on)
aws iam update-access-key --user-name ci-intern \
  --access-key-id $KEY --status Inactive
# 2 Investigate: every API call this key made, newest first
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=AccessKeyId,AttributeValue=$KEY \
  --max-results 20 \
  --query "Events[].[EventTime,EventName]" --output table
# 3 Eradicate: once the new key works, delete the old one
aws iam delete-access-key --user-name ci-intern --access-key-id $KEY

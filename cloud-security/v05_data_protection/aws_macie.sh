# Illustrative, not run here: check the current docs
aws macie2 enable-macie
aws macie2 create-classification-job --job-type ONE_TIME \
  --name store-exports-scan \
  --s3-job-definition '{"bucketDefinitions":[{
  "accountId":"<account-id>","buckets":["store-order-exports"]}]}'
aws macie2 list-findings --finding-criteria \
  '{"criterion":{"severity.description":{"eq":["High"]}}}'

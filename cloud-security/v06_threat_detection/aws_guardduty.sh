# Illustrative, not run here: check the current docs
aws guardduty create-detector --enable \
  --finding-publishing-frequency FIFTEEN_MINUTES
aws guardduty list-findings --detector-id <detector-id> \
  --finding-criteria '{"Criterion":{"severity":{"Gte":7}}}'
# send high findings to the on-call team's SNS topic
aws events put-rule --name guardduty-high --event-pattern '{
  "source":["aws.guardduty"],"detail-type":["GuardDuty Finding"],
  "detail":{"severity":[{"numeric":[">=",7]}]}}'
aws events put-targets --rule guardduty-high \
  --targets 'Id=oncall,Arn=arn:aws:sns:ap-south-1:<account-id>:oncall'

# Illustrative, not run here: check the current docs
# The school app's database password lives here, not in the code
aws secretsmanager create-secret \
  --name school/prod/db-password \
  --secret-string '<generated-by-your-pipeline>'
aws secretsmanager rotate-secret \
  --secret-id school/prod/db-password \
  --rotation-lambda-arn arn:aws:lambda:ap-south-1:111122223333:function:rot \
  --rotation-rules AutomaticallyAfterDays=30

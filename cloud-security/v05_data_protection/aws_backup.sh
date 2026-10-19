# Illustrative, not run here: check the current docs
aws backup create-backup-vault --backup-vault-name school-vault
aws backup put-backup-vault-lock-configuration \
  --backup-vault-name school-vault \
  --min-retention-days 30 --max-retention-days 365 \
  --changeable-for-days 3
# after 3 days the lock is fixed: nobody, not even root, can remove it
aws backup create-backup-plan --backup-plan '{
  "BackupPlanName":"school-daily","Rules":[{"RuleName":"daily",
  "TargetBackupVaultName":"school-vault",
  "ScheduleExpression":"cron(0 20 * * ? *)",
  "Lifecycle":{"DeleteAfterDays":35}}]}'

# Illustrative, not run here: check the current docs
# Vault Lock: nobody, not even an admin, deletes backups early
aws backup put-backup-vault-lock-configuration \
  --backup-vault-name hospital-records \
  --min-retention-days 7 \
  --max-retention-days 90 \
  --changeable-for-days 3
aws backup describe-backup-vault --backup-vault-name hospital-records \
  --query "{locked:Locked, min:MinRetentionDays, max:MaxRetentionDays}"

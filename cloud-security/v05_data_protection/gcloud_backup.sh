# Illustrative, not run here: check the current docs
gcloud backup-dr backup-vaults create school-vault \
  --location=asia-south1 --backup-min-enforced-retention=p30d
gcloud backup-dr backup-plans create school-daily \
  --location=asia-south1 --backup-vault=school-vault \
  --resource-type=compute.googleapis.com/Instance \
  --backup-rule=rule-id=daily,retention-days=30,recurrence=DAILY,\
backup-window-start=1,backup-window-end=7
# then attach the plan to the school's records server

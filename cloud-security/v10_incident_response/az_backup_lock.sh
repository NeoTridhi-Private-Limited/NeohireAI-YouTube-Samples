# Illustrative, not run here: check the current docs
# Immutable vault: "Locked" cannot be reversed, so test with Unlocked first
az backup vault update \
  --name hospital-vault --resource-group rg-backup \
  --immutability-state Locked
# Soft delete that cannot be switched off: deleted backups are kept
az backup vault backup-properties set \
  --name hospital-vault --resource-group rg-backup \
  --soft-delete-feature-state AlwaysOn \
  --soft-delete-duration 30

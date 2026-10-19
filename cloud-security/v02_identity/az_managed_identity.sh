# Illustrative, not run here: check the current docs
# The reports app gets its own identity: no secret in its code
az webapp identity assign \
  --name bank-reports-app \
  --resource-group rg-reports \
  --role "Storage Blob Data Reader" \
  --scope "/subscriptions/<subscription-id>/resourceGroups/rg-reports"

# Illustrative, not run here: check the current docs
# The intern reads one resource group, nothing else
az role assignment create \
  --assignee intern@example.com \
  --role "Reader" \
  --scope "/subscriptions/<subscription-id>/resourceGroups/rg-reports"

az role assignment list --assignee intern@example.com \
  --all --output table

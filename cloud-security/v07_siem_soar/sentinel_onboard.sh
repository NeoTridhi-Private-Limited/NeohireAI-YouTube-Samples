# Illustrative, not run here: check the current docs
# A Log Analytics workspace with 180 days retention, then Sentinel on it
az group create --name rg-soc --location centralindia
az monitor log-analytics workspace create \
  --resource-group rg-soc \
  --workspace-name law-soc \
  --retention-time 180
az sentinel onboarding-state create \
  --resource-group rg-soc \
  --workspace-name law-soc \
  --name default

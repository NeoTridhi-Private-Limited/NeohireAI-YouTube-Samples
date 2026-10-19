# Illustrative, not run here: check the current docs
# Turn on the Defender for Containers plan for the subscription
az security pricing create --name Containers --tier standard
# A private registry for the shop's images
az acr create \
  --name shopregistry \
  --resource-group rg-shop \
  --sku Premium
# Pods read secrets from Key Vault, not from the image
az aks enable-addons \
  --addons azure-keyvault-secrets-provider \
  --name aks-shop \
  --resource-group rg-shop

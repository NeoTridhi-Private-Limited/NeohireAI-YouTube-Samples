# Illustrative, not run here: check the current docs
az keyvault create --name kv-hospital-prod --resource-group rg-hospital \
  --location centralindia --sku premium --enable-purge-protection true
az keyvault key create --vault-name kv-hospital-prod --name reports-key \
  --kty RSA-HSM --size 3072
# rotation.json: rotate 90 days after creation, notify 30 days before expiry
az keyvault key rotation-policy update --vault-name kv-hospital-prod \
  --name reports-key --value rotation.json
# the storage account's managed identity needs access to the key first
az storage account update --name sthospitalreports -g rg-hospital \
  --encryption-key-source Microsoft.Keyvault \
  --encryption-key-vault https://kv-hospital-prod.vault.azure.net \
  --encryption-key-name reports-key
az storage account update --name sthospitalreports -g rg-hospital \
  --allow-blob-public-access false

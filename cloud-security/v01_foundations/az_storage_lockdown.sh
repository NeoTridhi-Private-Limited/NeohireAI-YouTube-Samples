# Illustrative, not run here: check the current docs
# Hospital scans: no anonymous blob access, HTTPS and TLS 1.2
az storage account update \
  --name hospitalscans \
  --resource-group rg-radiology \
  --allow-blob-public-access false \
  --https-only true \
  --min-tls-version TLS1_2

az storage account show --name hospitalscans \
  --resource-group rg-radiology \
  --query "{public:allowBlobPublicAccess, tls:minimumTlsVersion}"

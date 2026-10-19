# Illustrative, not run here: check the current docs
# Turn on Defender for Cloud plans for storage and servers
az account set --subscription "<subscription-id>"

az security pricing create -n StorageAccounts --tier standard
az security pricing create -n VirtualMachines --tier standard

az security pricing show -n StorageAccounts --query pricingTier

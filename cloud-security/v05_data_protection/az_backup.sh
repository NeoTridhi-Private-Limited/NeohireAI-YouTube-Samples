# Illustrative, not run here: check the current docs
az backup vault create --name rsv-school --resource-group rg-school \
  --location centralindia
az backup protection enable-for-vm --vault-name rsv-school \
  --resource-group rg-school --vm vm-school-records \
  --policy-name DefaultPolicy
az backup vault update --name rsv-school --resource-group rg-school \
  --immutability-state Unlocked
# test a restore first. Locked can never be undone.
az backup vault update --name rsv-school --resource-group rg-school \
  --immutability-state Locked

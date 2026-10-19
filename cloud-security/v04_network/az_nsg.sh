# Illustrative, not run here: check the current docs
az network nsg create -g rg-school -n nsg-db
# Only the app subnet may reach SQL on port 1433
az network nsg rule create -g rg-school --nsg-name nsg-db \
  -n allow-sql-from-app --priority 200 --direction Inbound \
  --access Allow --protocol Tcp \
  --source-address-prefixes 10.0.1.0/24 \
  --destination-port-ranges 1433
# Never RDP straight from the internet
az network nsg rule create -g rg-school --nsg-name nsg-db \
  -n deny-rdp-internet --priority 300 --direction Inbound \
  --access Deny --protocol Tcp --source-address-prefixes Internet \
  --destination-port-ranges 3389
az network vnet subnet update -g rg-school --vnet-name vnet-school \
  -n snet-db --network-security-group nsg-db

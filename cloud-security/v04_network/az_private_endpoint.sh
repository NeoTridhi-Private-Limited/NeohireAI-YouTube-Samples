# Illustrative, not run here: check the current docs
# Reach the SQL server on a private IP, then switch off public access
SQL_ID=$(az sql server show -g rg-portal -n sql-portal --query id -o tsv)
az network private-endpoint create -g rg-portal -n pe-sql \
  --vnet-name vnet-portal --subnet snet-data \
  --private-connection-resource-id "$SQL_ID" \
  --group-id sqlServer --connection-name sql-private
# Private DNS, so the usual server name resolves to the private IP
az network private-dns zone create -g rg-portal \
  -n privatelink.database.windows.net
az network private-dns link vnet create -g rg-portal -n link-portal \
  -z privatelink.database.windows.net -v vnet-portal -e false
az network private-endpoint dns-zone-group create -g rg-portal \
  --endpoint-name pe-sql -n default --zone-name sql \
  --private-dns-zone privatelink.database.windows.net
az sql server update -g rg-portal -n sql-portal \
  --enable-public-network false

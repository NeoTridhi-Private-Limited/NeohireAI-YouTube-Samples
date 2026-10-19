# Illustrative, not run here: check the current docs
# Built-in policy "Allowed locations", assigned to a management group
cat > params.json <<'EOF'
{"listOfAllowedLocations": {"value": ["centralindia", "southindia"]}}
EOF
MG="/providers/Microsoft.Management/managementGroups/hospital-prod"
az policy assignment create \
  --name allowed-locations-india \
  --display-name "Allowed locations: India only" \
  --policy e56962a6-4747-49cd-b67b-bf8b01975c4c \
  --scope "$MG" \
  --params @params.json

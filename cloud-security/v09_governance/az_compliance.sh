# Illustrative, not run here: check the current docs
# Detective view: which resources break our policies right now?
az policy state summarize --management-group hospital-prod --top 3
az policy state list \
  --management-group hospital-prod \
  --filter "complianceState eq 'NonCompliant'" \
  --query "[].{resource:resourceId, policy:policyDefinitionName}" \
  --output table

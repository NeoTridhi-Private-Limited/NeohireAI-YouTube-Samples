# Illustrative, not run here: check the current docs
# Many failed sign-ins for one user from one address, in the last hour
QUERY='SigninLogs
| where TimeGenerated > ago(1h)
| where ResultType != "0"
| summarize Failures = count() by UserPrincipalName, IPAddress
| where Failures > 10'
az monitor log-analytics query \
  --workspace <workspace-guid> \
  --analytics-query "$QUERY" \
  --output table

# Illustrative, not run here: check the current docs
# Admins need MFA and a compliant device. Start in report-only mode.
cat > ca.json <<'EOF'
{
  "displayName": "Admins need MFA and a compliant device",
  "state": "enabledForReportingButNotEnforced",
  "conditions": {
    "users": { "includeRoles": ["62e90394-69f5-4237-9190-012177145e10"],
               "excludeUsers": ["<break-glass-user-id>"] },
    "applications": { "includeApplications": ["All"] },
    "clientAppTypes": ["all"]
  },
  "grantControls": { "operator": "AND",
                     "builtInControls": ["mfa", "compliantDevice"] }
}
EOF
az rest --method post --body @ca.json \
  --url https://graph.microsoft.com/v1.0/identity/conditionalAccess/policies

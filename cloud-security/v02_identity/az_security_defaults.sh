# Illustrative, not run here: check the current docs
# A small tenant: are security defaults (M F A for all) on?
# Larger tenants use Conditional Access instead: next video.
G="https://graph.microsoft.com/v1.0/policies"
az rest --method get \
  --url "$G/identitySecurityDefaultsEnforcementPolicy" \
  --query isEnabled

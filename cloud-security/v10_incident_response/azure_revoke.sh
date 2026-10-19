# Illustrative, not run here: check the current docs
U=admin@example.com
G=https://graph.microsoft.com/v1.0
# 1 Contain: block sign-in for the phished admin account
az ad user update --id $U --account-enabled false
# 2 End every session and refresh token the attacker may hold
az rest --method POST --url "$G/users/$U/revokeSignInSessions"
# 3 Investigate: read this user's sign-in and audit logs in Entra
#   or Sentinel, and remove any MFA method the attacker added

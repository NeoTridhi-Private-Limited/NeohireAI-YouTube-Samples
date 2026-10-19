# Cloud Security: Microsoft, Google, AWS. Identity: working sample

Small files shown in the video. The Python files really run (standard library only, deterministic).
The shell files are illustrative configuration examples: they are NOT run in the video. Check the current
Microsoft Learn, Google Cloud and AWS documentation before using them, and replace every placeholder
(`<subscription-id>`, `<account-id>`, `<leaked-access-key-id>`, `my-project`, example.com names) with your own.
Never put real keys or passwords in these files.

Run a Python file from this folder:

    python least_priv.py

| File | Shows |
|---|---|
| key_age.py | find risky long-lived access keys: leaked, older than 90 days, or unused |
| least_priv.py | a tiny policy evaluator: explicit deny wins, then allow, otherwise denied |
| break_glass.py | check emergency admin accounts: phishing-resistant M F A, sign-in alert, tested in 90 days |
| aws_leaked_key.sh | AWS: deactivate a leaked key, check CloudTrail, then delete it |
| gcp_no_sa_keys.sh | Google Cloud: org policy against service account key creation; list existing keys |
| az_managed_identity.sh | Azure: a managed identity with one narrow role, no secret in code |
| aws_identity_center.sh | AWS: sign in through IAM Identity Center with short-lived credentials |
| az_role_assign.sh | Azure: Reader on one resource group |
| gcp_role_bind.sh | Google Cloud: remove basic Editor, grant object viewer to a group |
| aws_least_priv.sh | AWS: a read-only policy with an explicit deny on salary files |
| az_security_defaults.sh | Azure: check security defaults through Microsoft Graph |
| aws_require_mfa.sh | AWS: deny most actions when M F A is not present |
| gcp_owner_audit.sh | Google Cloud: who holds the owner role on a project |

Product names change often: check the current docs.

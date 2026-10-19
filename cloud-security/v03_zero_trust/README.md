# Cloud Security series: Zero Trust access (working sample)

Pure Python 3, standard library only. Each file runs on its own and prints the same output every time.

| File | What it shows |
| --- | --- |
| `ca_decision.py` | A toy Conditional Access engine: every matching policy adds a demand, a block always wins |
| `posture_check.py` | Device posture: encryption, screen lock, patch level and an EDR agent, scored per device |
| `session_check.py` | Why one check at sign-in is not enough: a stolen laptop with a still-valid token |

Run: `python ca_decision.py` (or any of the three).

## Configuration examples (illustrative, not run)

These show real command and policy syntax for each cloud, with placeholders. They were not run against a live
tenant. Product names, flags and defaults change often: check the current docs before you use them.

| File | Cloud | What it does |
| --- | --- | --- |
| `entra_ca.sh` | Microsoft | A Conditional Access policy via Microsoft Graph (`az rest`): admins need MFA and a compliant device, break-glass account excluded, report-only |
| `gcp_access_level.sh` | Google Cloud | An Access Context Manager access level: corp-owned, encrypted, screen-locked Windows laptops in India |
| `gcp_iap.sh` | Google Cloud | Identity-Aware Proxy on a backend service, granted to a group only with that access level |
| `aws_verified_access.sh` | AWS | A Verified Access instance, an IAM Identity Center trust provider and a group with a Cedar policy |

Sources: Microsoft Learn, Google Cloud documentation, AWS documentation (explained in our own words).

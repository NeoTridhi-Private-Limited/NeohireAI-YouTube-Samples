# Cloud Security series: Network security (working sample)

Pure Python 3, standard library only. Each file runs on its own and prints the same output every time.

| File | What it shows |
| --- | --- |
| `rule_matcher.py` | NSG-style rules: lowest priority number first, first match wins, then a default deny (simplified) |
| `stateful.py` | Why a security group lets the reply out by itself, and a network ACL needs an outbound rule |
| `rate_limit.py` | A WAF-style rate rule: a shopper is never blocked, a login bot is blocked after five tries |

Run: `python rule_matcher.py` (or any of the three).

## Configuration examples (illustrative, not run)

Real command syntax with placeholders, not run against live accounts. Check the current docs before use.

| File | Cloud | What it does |
| --- | --- | --- |
| `az_nsg.sh` | Microsoft | An NSG on the database subnet: SQL only from the app subnet, RDP from the internet denied |
| `az_waf.sh` | Microsoft | An Application Gateway WAF policy in Prevention mode, with the bot manager rule set |
| `az_private_endpoint.sh` | Microsoft | A Private Endpoint for Azure SQL, private DNS, public network access switched off |
| `gcp_firewall.sh` | Google Cloud | VPC firewall rules: HTTPS from load balancer ranges, MySQL by service account, SSH only via IAP |
| `gcp_cloud_armor.sh` | Google Cloud | A Cloud Armor policy: preconfigured SQL injection rule and a login throttle |
| `gcp_psc.sh` | Google Cloud | A Private Service Connect endpoint for Google APIs |
| `aws_sg_nacl.sh` | AWS | Security groups (database only from the web tier) and stateless NACL entries |
| `aws_waf.sh` | AWS | An AWS WAF web ACL with a managed SQL injection rule group and a rate-based rule |
| `aws_privatelink.sh` | AWS | VPC endpoints: a gateway endpoint for S3 and an interface endpoint (PrivateLink) for Secrets Manager |

Sources: Microsoft Learn, Google Cloud documentation, AWS documentation (explained in our own words).

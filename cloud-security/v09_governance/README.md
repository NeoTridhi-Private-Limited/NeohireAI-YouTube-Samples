# Cloud Security, Video 9: Governance and compliance (sample files)

Runnable (pure Python 3, standard library, deterministic):

| File | Shows |
| --- | --- |
| policy_check.py | policy as code: deny deployments outside India regions, public, or without an owner tag |
| cis_score.py | a CIS-style benchmark report: pass counts per section, a score, the fixes |
| data_map.py | a personal data map for a school app: purpose, consent, retention, children's data |

Run from this folder: `python policy_check.py` (and the same for the others).

Configuration examples (illustrative, not run here; check the current docs before use):

| File | Cloud | Shows |
| --- | --- | --- |
| az_policy.sh | Microsoft | Azure Policy "Allowed locations" assigned to a management group |
| gcp_org_policy.sh | Google Cloud | Organization Policy: public access prevention, resource locations |
| aws_scp.sh | AWS | a service control policy limiting regions to ap-south-1 / ap-south-2 |
| az_compliance.sh | Microsoft | policy compliance summary and non-compliant resources |
| gcp_scc.sh | Google Cloud | Security Command Center findings for public buckets |
| aws_config.sh | AWS | an AWS Config managed rule for public-read S3 buckets |
| aws_cis.sh | AWS | enabling the CIS AWS Foundations Benchmark in Security Hub |

Placeholders only (`<subscription-id>`-style IDs, my-project, example.com). No real secrets.
Privacy laws (India's DPDP Act, EU GDPR) are covered at a high level only. This is not legal advice:
check with your legal team.

Sources: Microsoft Learn, Google Cloud documentation, AWS documentation. Product names change often.

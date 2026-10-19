# Cloud Security: Microsoft, Google, AWS. Foundations: working sample

Small files shown in the video. The Python files really run (standard library only, deterministic).
The shell files are illustrative configuration examples: they are NOT run in the video. Check the current
Microsoft Learn, Google Cloud and AWS documentation before using them, and replace every placeholder
(`<subscription-id>`, `<account-id>`, `my-project`, bucket and account names) with your own.

Run a Python file from this folder:

    python shared_resp.py

| File | Shows |
|---|---|
| shared_resp.py | shared responsibility: who owns which duty in on-premises, IaaS, PaaS and SaaS |
| layers.py | defence in depth: 1,000 phishing emails against an online store, layer by layer |
| zero_trust.py | a tiny Zero Trust decision: M F A, device health, role; the network earns no trust |
| az_storage_lockdown.sh | Azure: no anonymous blob access, HTTPS only, TLS 1.2 |
| gcs_lockdown.sh | Google Cloud: public access prevention and uniform bucket-level access |
| s3_block_public.sh | AWS: S3 Block Public Access on a bucket and the whole account |
| az_defender_on.sh | Azure: Defender for Cloud plans for storage and servers |
| gcp_scc_on.sh | Google Cloud: Security Command Center API and active findings |
| aws_detect_on.sh | AWS: GuardDuty detector, Security Hub, high-severity findings |

Product names change often: check the current docs.

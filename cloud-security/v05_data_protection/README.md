# Cloud Security, Video 5: Data protection (working sample)

Runnable teaching programs (Python 3 standard library only, deterministic):

| File | Shows |
| --- | --- |
| envelope.py | envelope encryption with a toy cipher: data key, master key, rotation, crypto-shredding |
| dlp_scan.py | a tiny DLP scanner: PAN, Aadhaar-style and card patterns, with a Luhn checksum |
| restore_check.py | which backups survive a stolen admin account: plain, soft-delete and locked vaults |

Run one from this folder:

    python envelope.py

The toy cipher (XOR with a SHA-256 keystream) is for teaching only. Never use it for real data.
All numbers in the samples are made up (4111 1111 1111 1111 is a well-known test card number).

Configuration examples (illustrative, NOT run here; check the current docs before using):

| File | Cloud | Shows |
| --- | --- | --- |
| az_keyvault.sh, rotation.json | Microsoft | Key Vault, key rotation policy, customer-managed key for storage, public blob access off |
| gcloud_kms.sh | Google Cloud | Cloud KMS key ring and key with rotation, CMEK for a bucket, public access prevention |
| aws_kms.sh | AWS | KMS key with rotation, default bucket encryption with the key, S3 Block Public Access |
| purview_dlp.ps1 | Microsoft | Purview DLP policy and rule for credit card numbers, test mode first |
| gcp_dlp.tf | Google Cloud | Sensitive Data Protection inspect template for Aadhaar, PAN and cards |
| aws_macie.sh | AWS | Macie one-time classification job and high-severity findings |
| az_backup.sh | Microsoft | Recovery Services vault, VM protection, immutability unlocked then locked |
| gcloud_backup.sh | Google Cloud | Backup and DR backup vault with enforced retention, daily plan |
| aws_backup.sh | AWS | Backup vault, Vault Lock (compliance mode after 3 days), daily plan |

Placeholders such as <key-id>, <account-id>, my-project are not real values. Never put real secrets in files.
Sources: Microsoft Learn, Google Cloud documentation, AWS documentation. Product names change often.

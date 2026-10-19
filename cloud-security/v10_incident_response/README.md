# Cloud Security, Video 10: Incident response and the security programme (sample files)

Runnable (pure Python 3, standard library, deterministic):

| File | Shows |
| --- | --- |
| key_leak.py | after a leaked access key: what the attacker did before the key was disabled, and the exposure window |
| ransomware_timeline.py | a hospital ransomware timeline: time to detect, contain, report (CERT-In 6-hour check) |
| roadmap.py | a posture roadmap: progress and next three steps for a small, a mid-size and a large organisation |

Run from this folder: `python key_leak.py` (and the same for the others).

Configuration examples (illustrative, not run here; check the current docs before use):

| File | Cloud | Shows |
| --- | --- | --- |
| aws_key.sh | AWS | deactivate a leaked access key, search CloudTrail, delete the key |
| gcp_key.sh | Google Cloud | disable a service account key, read its audit logs |
| azure_revoke.sh | Microsoft | disable a phished Entra ID user and revoke sign-in sessions |
| aws_backup_lock.sh | AWS | AWS Backup Vault Lock |
| az_backup_lock.sh | Microsoft | immutable Recovery Services vault and always-on soft delete |
| gcs_backup_lock.sh | Google Cloud | a locked bucket retention policy for backup files |

Warning: Vault Lock (after its grace period), a Locked immutable vault and a locked bucket retention policy
cannot be undone. Try them on test resources first.
Reporting duties (CERT-In, sector regulators, DPDP Act, GDPR) are mentioned at a high level only.
This is not legal advice: check with your legal team.

Sources: Microsoft Learn, Google Cloud documentation, AWS documentation. Product names change often.

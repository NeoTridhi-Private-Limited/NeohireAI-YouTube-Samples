# Cloud Security, Video 6: Threat detection and posture management (working sample)

Runnable teaching programs (Python 3 standard library only, deterministic):

| File | Shows |
| --- | --- |
| posture_score.py | a weighted posture score, like a secure score, and the effect of fixing the top two findings |
| threat_detect.py | spotting a leaked access key by behaviour: new region, odd hour, new calls, server burst, logs off |
| triage.py | ranking findings by severity x internet exposure x customer data, not by severity alone |

Run one from this folder:

    python posture_score.py

Configuration examples (illustrative, NOT run here; check the current docs before using):

| File | Cloud | Shows |
| --- | --- | --- |
| az_posture.sh | Microsoft | Defender CSPM plan, secure score, controls and recommendations |
| gcloud_posture.sh | Google Cloud | Security Command Center findings: misconfigurations, public bucket, open SSH |
| aws_posture.sh | AWS | Security Hub CSPM with default standards, failed critical findings |
| az_threats.sh | Microsoft | Defender plans: Servers P2, Storage, Key Vault, Resource Manager; alerts |
| gcp_threats.tf | Google Cloud | Pub/Sub topic and SCC notification for high-severity THREAT findings |
| aws_guardduty.sh | AWS | GuardDuty detector, high findings, EventBridge rule to the on-call SNS topic |

Placeholders such as <subscription-id>, <detector-id>, 123456789, my-project are not real values.
Sources: Microsoft Learn, Google Cloud documentation, AWS documentation. Product names change often.

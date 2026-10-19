# Cloud Security, Video 7: Logging, SIEM and SOAR

Small samples for the video. The `.py` files are pure Python (standard library only) and really run.
The `.sh`, `.yaral` and `.json` files are illustrative configuration for each cloud: not run here, check the current docs.

Run a Python sample from this folder:

    python kql_like.py

| File | What it shows |
|---|---|
| kql_like.py | A KQL-like filter: failed sign-ins per user and address, alert above ten (a UPI app at 2 am) |
| correlate.py | Correlation: login, new access key, logging stopped, by one account within 30 minutes (a hospital) |
| playbook.py | A SOAR playbook: safe steps run automatically, the risky step waits for a person |
| sentinel_detect.sh | Microsoft Sentinel: the failed sign-in query in KQL, run with the Azure CLI |
| sentinel_onboard.sh | Microsoft: a Log Analytics workspace with 180 days retention, Sentinel turned on |
| many_failed_logins.yaral | Google Security Operations: the same detection as a YARA-L 2.0 rule |
| gcp_audit_sink.sh | Google Cloud: every audit log in the organisation sent to one BigQuery dataset |
| aws_org_trail.sh | AWS: one multi-region organisation trail with log file validation and a KMS key |
| trail_tamper.sh, trail_tamper.json | AWS: an EventBridge rule that pages the SOC when the trail is stopped or deleted |

Sources: Microsoft Learn, Google Cloud documentation, AWS documentation. Product names change often.
All names, addresses (203.0.113.x, 198.51.100.x are documentation ranges) and account IDs are placeholders.

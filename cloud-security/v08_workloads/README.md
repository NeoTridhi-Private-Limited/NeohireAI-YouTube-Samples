# Cloud Security, Video 8: Workloads, containers and supply chain

Small samples for the video. The `.py` files are pure Python (standard library only) and really run.
The `.sh` and `.yaml` files are illustrative configuration for each cloud: not run here, check the current docs.

Run a Python sample from this folder:

    python admission.py

| File | What it shows |
|---|---|
| admission.py | An admission check like Binary Authorization: trusted registry, signed, digest not latest, no critical holes |
| sbom_check.py | SBOMs turn "which apps use the vulnerable library?" into a search (a bank) |
| secret_scan.py | A tiny pre-commit secret scanner (a school app); the AWS key is AWS's published example key |
| binauthz_policy.yaml | Google Cloud: a Binary Authorization policy requiring a CI attestation |
| gke_binauthz.sh | Google Cloud: turn on scanning, import the policy, enforce it on a GKE cluster |
| defender_containers.sh | Microsoft: Defender for Containers plan, a private ACR, the Key Vault secrets provider on AKS |
| aws_inspector.sh | AWS: Amazon Inspector, continuous ECR scanning, immutable tags |
| aws_secret.sh | AWS: the database password in Secrets Manager, rotated every 30 days |
| pod_hardening.yaml | Any cloud (AKS, GKE, EKS): a pod with a digest, non-root, read-only, no capabilities |

Sources: Microsoft Learn, Google Cloud documentation, AWS documentation. Product names change often.
All names, registries and account IDs are placeholders; never put real secrets in code.

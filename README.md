# NeohireAI YouTube Samples

Working sample code for the videos on the [NeoTridhi YouTube channel](https://youtube.com/@neotridhi).
Every sample is plain Python 3.10+ and runs offline: a small stand-in model answers each call, so you can
see the ideas work without an API key. Each folder's README shows how to plug in a real model.

## The Agent Reading List

Eight famous readings about AI agents, explained in our own words, one long video each.
Playlist: https://www.youtube.com/playlist?list=PLMxleK2kIm3E

| # | Video | Original reading | Sample |
|---|---|---|---|
| 1 | [Building Effective Agents Explained](https://www.youtube.com/watch?v=ooctxsWs19w) | Anthropic, Building Effective Agents | [v01_building_effective_agents](agent-reading-list/v01_building_effective_agents) |
| 2 | [Context Engineering for AI Agents](https://www.youtube.com/watch?v=_NpiIJobR6A) | Anthropic, Effective Context Engineering | [v02_context_engineering](agent-reading-list/v02_context_engineering) |
| 3 | [OpenAI's Practical Guide to Building Agents](https://www.youtube.com/watch?v=iwoAMA7di2g) | OpenAI, A Practical Guide to Building Agents | [v03_practical_guide_agents](agent-reading-list/v03_practical_guide_agents) |
| 4 | [Google's AI Agents Whitepaper Explained](https://www.youtube.com/watch?v=DdrmDHv_shk) | Google, Agents whitepaper | [v04_google_agents_whitepaper](agent-reading-list/v04_google_agents_whitepaper) |
| 5 | [LLM Powered Autonomous Agents](https://www.youtube.com/watch?v=S8VsASdPQL4) | Lilian Weng, LLM Powered Autonomous Agents | [v05_autonomous_agents](agent-reading-list/v05_autonomous_agents) |
| 6 | [7 Patterns for LLM Systems](https://www.youtube.com/watch?v=eaZBQ189bsU) | Eugene Yan, Patterns for Building LLM-based Systems | [v06_llm_patterns](agent-reading-list/v06_llm_patterns) |
| 7 | [Your AI Product Needs Evals](https://www.youtube.com/watch?v=KkCtx5uLOAA) | Hamel Husain, Your AI Product Needs Evals | [v07_evals](agent-reading-list/v07_evals) |
| 8 | [Neural Networks Zero to Hero](https://www.youtube.com/watch?v=OPtVDOZxu_g) | Andrej Karpathy, Neural Networks: Zero to Hero | [v08_zero_to_hero](agent-reading-list/v08_zero_to_hero) |

## Cloud Security: Microsoft vs Google Cloud vs AWS

A complete cloud security programme, each control shown in Azure, Google Cloud and AWS.
Playlist: https://www.youtube.com/playlist?list=PLaQnnozboy20

The Python files run offline (standard library only). The shell, Terraform and policy files are
illustrative configuration examples that were not run: check the current Microsoft, Google Cloud and AWS
documentation and replace every placeholder before you use them.

| # | Video | Sample |
|---|---|---|
| 1 | [Cloud Security Foundations](https://www.youtube.com/watch?v=ymNE2anxOB4) | [v01_foundations](cloud-security/v01_foundations) |
| 2 | [Cloud IAM Security](https://www.youtube.com/watch?v=inmMC0HYxSk) | [v02_identity](cloud-security/v02_identity) |
| 3 | [Zero Trust Explained](https://www.youtube.com/watch?v=A3G1OyioFLI) | [v03_zero_trust](cloud-security/v03_zero_trust) |
| 4 | [Cloud Network Security](https://www.youtube.com/watch?v=vYkvdS-gZEE) | [v04_network](cloud-security/v04_network) |
| 5 | [Cloud Data Protection](https://www.youtube.com/watch?v=7oehulSBDDs) | [v05_data_protection](cloud-security/v05_data_protection) |
| 6 | [Threat Detection and Posture (CSPM)](https://www.youtube.com/watch?v=G0mUGP33bgU) | [v06_threat_detection](cloud-security/v06_threat_detection) |
| 7 | [SIEM and SOAR Explained](https://www.youtube.com/watch?v=cdmIabGg6CI) | [v07_siem_soar](cloud-security/v07_siem_soar) |
| 8 | [Container and Supply Chain Security](https://www.youtube.com/watch?v=A4I4sPt-6DA) | [v08_workloads](cloud-security/v08_workloads) |
| 9 | [Cloud Governance](https://www.youtube.com/watch?v=RIA3b2r7isA) | [v09_governance](cloud-security/v09_governance) |
| 10 | [Cloud Incident Response](https://www.youtube.com/watch?v=cMqLRM7gsqs) | [v10_incident_response](cloud-security/v10_incident_response) |

## How to run

    git clone <this repository>
    cd NeohireAI-YouTube-Samples/agent-reading-list/v01_building_effective_agents
    python support_desk.py

Or use **Code > Download ZIP** on GitHub to get everything without git.

The videos are independent explanations, not affiliated with or endorsed by the authors of the readings;
please read the originals.

The sample code is our own, written for the videos, and is released under the [MIT License](LICENSE).
The articles, papers and courses it explains belong to their authors; this repository contains no text or code
copied from them. Where a sample follows the design of someone's open-source code, its README credits it.

NeoTridhi: AI training and AI solutions. NeohireAI: AI hiring for all industries. https://NeohireAI.com

# Illustrative, not run here: check the current docs
# Security Command Center is first activated for the
# organization in the console. Then, from the command line:
gcloud services enable securitycenter.googleapis.com \
  --project=my-project

gcloud scc findings list projects/my-project \
  --filter="state=\"ACTIVE\"" --limit=5

# Illustrative, not run here: check the current docs
SA=ci-deployer@my-project.iam.gserviceaccount.com
# 1 Find the leaked key, then disable it
gcloud iam service-accounts keys list --iam-account=$SA
gcloud iam service-accounts keys disable 1a2b3c4d5e6f7a8b \
  --iam-account=$SA
# 2 Investigate: what did this service account do in the last two days?
gcloud logging read \
  "protoPayload.authenticationInfo.principalEmail=\"$SA\"" \
  --project=my-project --freshness=2d --limit=20 \
  --format="table(timestamp, protoPayload.methodName)"

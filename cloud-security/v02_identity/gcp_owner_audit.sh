# Illustrative, not run here: check the current docs
# Who holds the owner role? It should be a few named people
gcloud projects get-iam-policy my-project \
  --flatten="bindings[].members" \
  --filter="bindings.role:roles/owner" \
  --format="table(bindings.members)"

# 2-Step Verification itself is enforced in the Google Admin
# console, under Security, Authentication.

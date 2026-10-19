# Illustrative, not run here: check the current docs
# Swap a broad basic role for a narrow one, granted to a group
gcloud projects remove-iam-policy-binding my-project \
  --member="user:intern@example.com" \
  --role="roles/editor"

gcloud projects add-iam-policy-binding my-project \
  --member="group:report-readers@example.com" \
  --role="roles/storage.objectViewer"

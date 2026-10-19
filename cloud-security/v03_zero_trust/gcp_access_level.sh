# Illustrative, not run here: check the current docs
# An access level: company-owned, encrypted, locked laptops in India
cat > level.yaml <<'EOF'
- devicePolicy:
    requireScreenlock: true
    requireCorpOwned: true
    allowedEncryptionStatuses:
      - ENCRYPTED
    osConstraints:
      - osType: DESKTOP_WINDOWS
        minimumVersion: 10.0.26100
  regions:
    - IN
EOF
gcloud access-context-manager levels create corp_laptops \
  --policy=<policy-id> --title="Corp laptops" \
  --basic-level-spec=level.yaml --combine-function=and

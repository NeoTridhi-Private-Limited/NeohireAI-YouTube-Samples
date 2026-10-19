# Illustrative, not run here: check the current docs
# Block every kind of public access, on the bucket and the account
CFG="BlockPublicAcls=true,IgnorePublicAcls=true"
CFG="$CFG,BlockPublicPolicy=true,RestrictPublicBuckets=true"

aws s3api put-public-access-block --bucket my-hospital-mri-scans \
  --public-access-block-configuration "$CFG"

aws s3control put-public-access-block --account-id "<account-id>" \
  --public-access-block-configuration "$CFG"

aws s3api get-public-access-block --bucket my-hospital-mri-scans

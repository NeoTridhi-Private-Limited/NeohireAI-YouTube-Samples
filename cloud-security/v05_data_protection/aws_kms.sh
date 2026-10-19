# Illustrative, not run here: check the current docs
aws kms create-key --description "hospital reports" \
  --key-usage ENCRYPT_DECRYPT --key-spec SYMMETRIC_DEFAULT
aws kms create-alias --alias-name alias/hospital-reports \
  --target-key-id <key-id>
aws kms enable-key-rotation --key-id <key-id> --rotation-period-in-days 90
aws s3api put-bucket-encryption --bucket hospital-reports \
  --server-side-encryption-configuration '{"Rules":[{
  "ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"aws:kms",
  "KMSMasterKeyID":"alias/hospital-reports"},"BucketKeyEnabled":true}]}'
aws s3api put-public-access-block --bucket hospital-reports \
  --public-access-block-configuration "BlockPublicAcls=true,\
IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"

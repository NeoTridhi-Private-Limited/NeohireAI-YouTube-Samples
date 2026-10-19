# Illustrative, not run here: check the current docs
# Continuous vulnerability scanning for images, instances and functions
aws inspector2 enable --resource-types ECR EC2 LAMBDA
aws ecr put-registry-scanning-configuration \
  --scan-type ENHANCED \
  --rules '[{"scanFrequency": "CONTINUOUS_SCAN",
    "repositoryFilters": [{"filter": "*", "filterType": "WILDCARD"}]}]'
# A tag, once pushed, can never point to a different image
aws ecr put-image-tag-mutability \
  --repository-name shop/web \
  --image-tag-mutability IMMUTABLE

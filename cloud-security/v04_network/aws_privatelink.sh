# Illustrative, not run here: check the current docs
# S3 through a gateway endpoint: no internet path needed
aws ec2 create-vpc-endpoint --vpc-id vpc-0abc \
  --vpc-endpoint-type Gateway \
  --service-name com.amazonaws.ap-south-1.s3 \
  --route-table-ids rtb-0abc
# Secrets Manager through an interface endpoint, which is PrivateLink
aws ec2 create-vpc-endpoint --vpc-id vpc-0abc \
  --vpc-endpoint-type Interface \
  --service-name com.amazonaws.ap-south-1.secretsmanager \
  --subnet-ids subnet-0abc --security-group-ids sg-0endpoint \
  --private-dns-enabled

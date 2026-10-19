# Illustrative, not run here: check the current docs
aws ec2 create-security-group --group-name web-sg \
  --description "Store web tier" --vpc-id vpc-0abc
aws ec2 authorize-security-group-ingress --group-id sg-0web \
  --protocol tcp --port 443 --cidr 0.0.0.0/0
# The database accepts only members of the web tier's security group
aws ec2 authorize-security-group-ingress --group-id sg-0db \
  --protocol tcp --port 3306 --source-group sg-0web
# Subnet NACL is stateless: allow HTTPS in, and replies out
aws ec2 create-network-acl-entry --network-acl-id acl-0abc \
  --ingress --rule-number 100 --protocol tcp --rule-action allow \
  --port-range From=443,To=443 --cidr-block 0.0.0.0/0
aws ec2 create-network-acl-entry --network-acl-id acl-0abc \
  --egress --rule-number 100 --protocol tcp --rule-action allow \
  --port-range From=1024,To=65535 --cidr-block 0.0.0.0/0

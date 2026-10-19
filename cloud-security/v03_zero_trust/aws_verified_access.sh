# Illustrative, not run here: check the current docs
aws ec2 create-verified-access-instance --description "bank apps"
aws ec2 create-verified-access-trust-provider \
  --trust-provider-type user \
  --user-trust-provider-type iam-identity-center \
  --policy-reference-name idc
aws ec2 attach-verified-access-trust-provider \
  --verified-access-instance-id vai-0abc \
  --verified-access-trust-provider-id vatp-0abc
cat > policy.cedar <<'EOF'
permit(principal, action, resource)
when {
  context.idc.groups has "<loan-officers-group-id>"
  && context.idc.user.email.verified == true
};
EOF
aws ec2 create-verified-access-group --verified-access-instance-id vai-0abc \
  --policy-document file://policy.cedar

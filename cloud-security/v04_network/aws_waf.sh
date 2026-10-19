# Illustrative, not run here: check the current docs
cat > rules.json <<'EOF'
[{"Name": "sqli", "Priority": 1, "OverrideAction": {"None": {}},
  "Statement": {"ManagedRuleGroupStatement":
    {"VendorName": "AWS", "Name": "AWSManagedRulesSQLiRuleSet"}},
  "VisibilityConfig": {"SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true, "MetricName": "sqli"}},
 {"Name": "ip-rate", "Priority": 2, "Action": {"Block": {}},
  "Statement": {"RateBasedStatement": {"Limit": 500,
    "AggregateKeyType": "IP"}},
  "VisibilityConfig": {"SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true, "MetricName": "ip-rate"}}]
EOF
VIS=SampledRequestsEnabled=true,CloudWatchMetricsEnabled=true,MetricName=shop
aws wafv2 create-web-acl --name shop-acl --scope REGIONAL \
  --default-action Allow={} --rules file://rules.json --visibility-config $VIS
aws wafv2 associate-web-acl --web-acl-arn <web-acl-arn> \
  --resource-arn <load-balancer-arn>

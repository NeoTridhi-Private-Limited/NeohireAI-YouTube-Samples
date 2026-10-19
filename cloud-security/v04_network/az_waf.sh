# Illustrative, not run here: check the current docs
# A WAF policy for the store's Application Gateway
# (it starts with Microsoft_DefaultRuleSet by default)
az network application-gateway waf-policy create -g rg-shop -n shop-waf
# Block, not just log, once you have watched it in Detection mode
az network application-gateway waf-policy policy-setting update \
  -g rg-shop --policy-name shop-waf --mode Prevention --state Enabled
# Add the managed bot protection rules for the sale
az network application-gateway waf-policy managed-rule rule-set add \
  -g rg-shop --policy-name shop-waf \
  --type Microsoft_BotManagerRuleSet --version 1.0
# Attach the policy to the gateway
WAF_ID=$(az network application-gateway waf-policy show -g rg-shop \
  -n shop-waf --query id -o tsv)
az network application-gateway update -g rg-shop -n shop-agw \
  --set firewallPolicy.id="$WAF_ID"

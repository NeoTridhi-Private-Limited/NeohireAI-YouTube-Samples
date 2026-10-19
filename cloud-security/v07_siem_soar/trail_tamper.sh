# Illustrative, not run here: check the current docs
# Page the SOC when anyone stops or deletes the audit trail
cat > trail_tamper.json <<'JSON'
{"source": ["aws.cloudtrail"],
 "detail-type": ["AWS API Call via CloudTrail"],
 "detail": {"eventSource": ["cloudtrail.amazonaws.com"],
            "eventName": ["StopLogging", "DeleteTrail"]}}
JSON
aws events put-rule \
  --name trail-tamper \
  --event-pattern file://trail_tamper.json
aws events put-targets \
  --rule trail-tamper \
  --targets Id=page-soc,Arn=arn:aws:sns:ap-south-1:111122223333:soc-alerts

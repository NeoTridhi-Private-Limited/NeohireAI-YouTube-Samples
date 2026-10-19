# Illustrative, not run here: check the current docs
Connect-IPPSSession
New-DlpCompliancePolicy -Name "Store customer data" `
  -ExchangeLocation All -SharePointLocation All -OneDriveLocation All `
  -Mode TestWithNotifications
New-DlpComplianceRule -Name "Block card numbers" `
  -Policy "Store customer data" `
  -ContentContainsSensitiveInformation @{Name="Credit Card Number"} `
  -BlockAccess $true
# after a week of watching the test results, switch it on
Set-DlpCompliancePolicy -Identity "Store customer data" -Mode Enable

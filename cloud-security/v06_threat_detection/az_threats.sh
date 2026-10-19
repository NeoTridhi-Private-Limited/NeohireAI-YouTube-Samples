# Illustrative, not run here: check the current docs
az security pricing create --name VirtualMachines --tier standard \
  --subplan P2
az security pricing create --name StorageAccounts --tier standard
az security pricing create --name KeyVaults --tier standard
# Defender for Resource Manager: odd management calls, like a stolen key
az security pricing create --name Arm --tier standard
az security pricing list --output table
az security alert list --output table

# Illustrative, not run here: check the current docs
az account set --subscription <subscription-id>
# Defender CSPM: attack paths, agentless scanning, more checks
az security pricing create --name CloudPosture --tier standard
az security secure-scores show --name ascScore
az security secure-score-controls list --output table
# every recommendation, healthy or not, per resource
az security assessment list --output table

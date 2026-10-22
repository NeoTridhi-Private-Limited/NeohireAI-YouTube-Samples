"""Deploy step: needs DEPLOY_TOKEN from the CI secret store."""
import os
import sys

if not os.environ.get("DEPLOY_TOKEN"):
    sys.exit("DEPLOY_TOKEN is missing: set it as a CI secret")
print("deploying dist/feeapp.zip to production")

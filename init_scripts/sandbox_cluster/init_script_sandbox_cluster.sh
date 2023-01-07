#!/bin/bash

set -e
set -o pipefail

# These environment variables would normally be set by Spark scripts
# However, for a Databricks init script, they have not been set yet.
# We will keep the names the same here, but not export them.
# These must be changed if the associated Spark environment variables
# are changed.
DB_HOME=/databricks
SPARK_HOME=$DB_HOME/spark
SPARK_CONF_DIR=$SPARK_HOME/conf

# Add to cluster-scoped environment variables
echo "export NOTEBOOK_MODE=true" >> "$SPARK_CONF_DIR/spark-env.sh"

# Install requirements
curl -u "$GITHUB_USER:$GITHUB_TOKEN" https://raw.github.tools.sap/BNA/platform-datalake-jobs/main/requirements.txt -o /tmp/requirements.txt
pip install -r /tmp/requirements.txt -i https://$ARTIFACTORY_USER:$ARTIFACTORY_TOKEN@common.repositories.cloud.sap/artifactory/api/pypi/sapbd-pypi/simple
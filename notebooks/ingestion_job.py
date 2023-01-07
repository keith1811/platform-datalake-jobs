# Databricks notebook source
# MAGIC %md
# MAGIC ### Ingestion job

# COMMAND ----------

!cp ../requirements.txt ~/.
%pip install -r ~/requirements.txt -i https://i319659:cmVmdGtuOjAxOjE3MDQzNDk0ODk6M1czemYyMWlDNDB6QlFNbHBKTTY4UHJGWTFm@common.repositories.cloud.sap/artifactory/api/pypi/sapbd-pypi/simple

# COMMAND ----------

# MAGIC %pip install https://i319659:cmVmdGtuOjAxOjE3MDQzNDk0ODk6M1czemYyMWlDNDB6QlFNbHBKTTY4UHJGWTFm@common.repositories.cloud.sap:443/artifactory/pypi-proxy-cache/d2/ac/556e4410326ce77eeb1d1ec35a3e3ec847fb3e5cb30673729d2eeeffc970/pytest-7.1.1-py3-none-any.whl

# COMMAND ----------

# MAGIC %pip install https://i319659:cmVmdGtuOjAxOjE3MDQzNDk0ODk6M1czemYyMWlDNDB6QlFNbHBKTTY4UHJGWTFm@common.repositories.cloud.sap/artifactory/api/pypi/pytest-7.1.1-py3-none-any.whl/simple 

# COMMAND ----------

# MAGIC %pip install https://i319659:cmVmdGtuOjAxOjE3MDQzNDk0ODk6M1czemYyMWlDNDB6QlFNbHBKTTY4UHJGWTFm@common.repositories.cloud.sap:443/artifactory/pypi-proxy-cache/.pypi/pyyaml.html

# COMMAND ----------

# MAGIC %sh
# MAGIC pip freeze | xargs pip uninstall -y

# COMMAND ----------

!cp ../requirements.txt ~/.
%pip install -r ~/requirements.txt

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %load_ext autoreload
# MAGIC %autoreload 2
# MAGIC 
# MAGIC from utils.sbnutils import SBNUtils
# MAGIC 
# MAGIC sbnutils = SBNUtils(dbutils)
# MAGIC sbnutils.log.info(f'cong test')
# MAGIC sbnutils.storage.get_location("raw")
# MAGIC sbnutils.kafka.broker.get_id()
# MAGIC sbnutils.kafka.schema_registry.get_id()
# MAGIC sbnutils.kafka.schema_registry.get_secret()

# COMMAND ----------

# MAGIC %run -m pytest -q "../tests/test_sample_streaming_job.py"

# COMMAND ----------

# MAGIC %run -m pytest "/Repos/c.du@sap.com/platform-datalake-jobs/tests/test_sample_streaming_job.py"

# COMMAND ----------



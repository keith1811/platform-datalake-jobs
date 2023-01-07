# Databricks notebook source
# MAGIC %md
# MAGIC ### Sample batch job

# COMMAND ----------

# MAGIC %load_ext autoreload
# MAGIC %autoreload 2
# MAGIC 
# MAGIC from utils.sbnutils import SBNUtils

# COMMAND ----------

sbnutils = SBNUtils(dbutils)
sbnutils.log.info(f'cong test')

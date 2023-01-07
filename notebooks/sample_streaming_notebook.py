# Databricks notebook source
# MAGIC %md
# MAGIC ### Sample streaming job
# MAGIC #### Setup

# COMMAND ----------

# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

# MAGIC %md
# MAGIC #### Import modules

# COMMAND ----------

# from utils.sbnutils import SBNUtils
from modules.sample_streaming_module import *

# COMMAND ----------

# MAGIC %md
# MAGIC #### JOb main part

# COMMAND ----------

# # Initialize the SBNUtils module with the dbutils object
# sbnutils = SBNUtils(dbutils)

# Run sample streaming job
sample_streaming_job()

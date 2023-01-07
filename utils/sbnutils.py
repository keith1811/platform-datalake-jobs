import os
import yaml

from pyspark.dbutils import DBUtils
from pyspark.sql import SparkSession


def log_info(message):
    notebook_mode, job_name, env, logger = _get_env()
    logger.info(message)


def log_error(message):
    notebook_mode, job_name, env, logger = _get_env()
    logger.error(message)


def get_storage_location(zone_type):
    config = _get_config()
    return config["zone_type"][zone_type]["storage_account_path"]


def get_database_name():
    config = _get_config()
    return config["database"]["name"]


def _get_env():
    spark = SparkSession.builder.getOrCreate()
    dbutils = DBUtils(spark)
    env_notebook_mode = os.getenv("NOTEBOOK_MODE")
    notebook_mode = (
        env_notebook_mode is not None and env_notebook_mode.lower() == "true"
    )
    if notebook_mode:
        job_name = (
            dbutils.notebook.entry_point.getDbutils()
            .notebook()
            .getContext()
            .notebookPath()
            .get()
        )
        env = "notebookdev"
    else:
        job_name = dbutils.widgets.getArgument("job_name")
        env = dbutils.widgets.getArgument("env")
    logger = spark._jvm.org.apache.log4j.Logger.getLogger(f"[{env}]-{job_name}")
    return notebook_mode, job_name, env, logger


def _get_config():
    notebook_mode, job_name, env, logger = _get_env()
    # Load environment configuration
    with open(f"../config/{env}.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config
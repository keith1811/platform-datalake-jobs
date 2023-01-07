# import pytest
# from unittest.mock import patch

# @patch('pyspark.dbutils')
# @patch('pyspark.sql.SparkSession')
# def test_get_location(dbutils, spark):
#     spark.builder.getOrCreate.return_value = "SparkSession"
#     dbutils.widgets.getArgument.side_effect = ['job_name', 'sandbox']
#     sbn_utils = SBNUtils(dbutils, notebook_mode=False)
#     assert sbn_utils.storage.get_location("raw") == "abfss://sc1man02-raw@bnasandboxsa.dfs.core.windows.net"

# @patch('pyspark.dbutils')
# @patch('pyspark.sql.SparkSession')
# def test_get_broker_url(dbutils, spark):
#     sbn_utils = SBNUtils(dbutils, notebook_mode=False)
#     assert sbn_utils.kafka.broker.get_url() == "lkc-vrp9g0-g4q7zp.westus2.azure.glb.confluent.cloud"

# @patch('pyspark.dbutils')
# @patch('pyspark.sql.SparkSession')
# def test_get_schema_registry_url(dbutils, spark):
#     sbn_utils = SBNUtils(dbutils, notebook_mode=False)
#     assert sbn_utils.kafka.schema_registry.get_url() == "https://psrc-3508o.westus2.azure.confluent.cloud"

# @patch('pyspark.dbutils')
# @patch('pyspark.sql.SparkSession')
# def test_get_database_name(dbutils, spark):
#     sbn_utils = SBNUtils(dbutils, notebook_mode=False)
#     assert sbn_utils.database.get_name() == "sc1man02_raw"
    
# @patch('pyspark.sql.SparkSession')
# def test_SBNUtils_init(spark_session):
#     dbutils = MagicMock()
#     sbn_utils = SBNUtils(dbutils, False)
#     assert sbn_utils.spark == spark_session
#     assert sbn_utils.notebook_mode == False
#     assert sbn_utils.job_name == 'mock-job-name'
#     assert sbn_utils.env == 'mock-env'
#     assert sbn_utils.config == 'mock-config'

# @patch('pyspark.sql.SparkSession.builder.getOrCreate')
# @patch('pyspark.dbutils.DBUtils.widgets.getArgument')
# @patch('pyspark.dbutils.DBUtils.widgets.get')
# @patch('yaml.safe_load')
# def test_SBNUtils_init_notebook_mode(mock_yaml_load, mock_get, mock_get_argument, mock_get_or_create, spark_session):
#     mock_yaml_load.return_value = 'mock-config'
#     mock_get_argument.return_value = 'mock-job-name'
#     mock_get.return_value = 'mock-env'
#     mock_get_or_create.return_value = spark_session
#     dbutils = MagicMock()
#     sbn_utils = SBNUtils(dbutils, True)
#     assert sbn_utils.spark == spark_session
#     assert sbn_utils.notebook_mode == True
#     assert sbn_utils.job_name == 'Notebook'
#     assert sbn_utils.env == 'notebookdev'
#     assert sbn_utils.config == 'mock-config'

import pytest
from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException
import mock
from modules.sample_streaming_module import *

@mock.patch('sample_streaming_module.sbnutils')
@mock.patch('sample_streaming_module.database_name', 'test_database')
@mock.patch('sample_streaming_module.table_name', 'test_table')
@mock.patch('sample_streaming_module.zone_type', 'test_zone')
def test_get_job_variables(mock_sbnutils, database_name, table_name, zone_type):
    # Set up mock return values for sbnutils functions
    mock_sbnutils.get_storage_location.return_value = 'test_location'
    
    table_full_name, table_location, sample_data_path = get_job_variables(database_name, table_name, zone_type)
    
    # Assert that the returned table_full_name is correct
    assert table_full_name == f"{database_name}.{table_name}"
    
    # Assert that the returned table_location starts with the correct raw_zone_location
    assert table_location.startswith(sbnutils.storage.get_location(zone_type))
    
    # Assert that the returned sample_data_path is a valid file path
    assert os.path.isabs(sample_data_path)
    assert os.path.exists(sample_data_path)

# # Mocked objects
# @patch("utils.sbnutils.SBNUtils")
# def test_sample_streaming_job(SBNUtilsMock):
#     # Initialize mock objects
#     spark = SparkSession.builder.getOrCreate()
#     dbutils = MagicMock()
#     sbnutils = SBNUtilsMock.return_value

#     # Mocked Spark SQL: CREATE DATABASE
#     sbnutils.spark.sql.return_value = None

#     # Mocked Spark SQL: DROP TABLE
#     sbnutils.spark.sql.side_effect = [None, None]

#     # Mocked DBUtils: rm
#     dbutils.fs.rm.return_value = None

#     # Mocked DeltaTable.createIfNotExists
#     sbnutils.DeltaTable.createIfNotExists.return_value.tableName.return_value.location.return_value.addColumns.return_value.execute.return_value = None

#     # Mocked readStream
#     sbnutils.spark.readStream.format.return_value.schema.return_value.option.return_value.option.return_value.option.return_value.load.return_value = spark.createDataFrame(
#         [("a", "b", 1), ("c", "d", 2), ("e", "f", 3)], ["col1", "col2", "col3"]
#     )

#     # Mocked writeStream
# #     sbnutils.spark.readStream.format.return_value.schema.return_value.option.return_value.option.return_value.option.return_value.load.return_value.writeStream.format.return_value.option.return_value.option.return_value.option.return_value

#     # Run sample streaming job
#     sample_streaming_job(spark, dbutils, sbnutils)

#     # Assertions
#     assert SBNUtilsMock.called
#     assert sbnutils.spark.sql.called
#     assert dbutils.fs.rm.called
#     assert sbnutils.DeltaTable.createIfNotExists.called
#     assert sbnutils.spark.readStream.format.called

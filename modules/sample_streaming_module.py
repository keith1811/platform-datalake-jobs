import os
from pyspark.dbutils import DBUtils
from pyspark.sql import SparkSession
from delta.tables import DeltaTable
import utils.sbnutils as sbnutils


def sample_streaming_job():
    database_name = "sample_data"
    table_name = "sample_streaming"
    # Zone type: "raw", "consumption", "staging", "enrichment", "export", etc.
    zone_type = "sample"

    # Create a SparkSession or get the active one
    spark = SparkSession.builder.getOrCreate()
    dbutils = DBUtils(spark)

    # Job Start
    sbnutils.log_info(f"Sample streaming job Start")

    # Get job variables
    table_full_name, table_location, sample_data_path = _get_job_variables(
        database_name, table_name, zone_type
    )

    # Create sample data datase
    spark.sql(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    spark.sql(f"USE DATABASE  {database_name}")

    # Drop the table and delete the data from storage
    spark.sql(f"DROP TABLE IF EXISTS {table_full_name}")
    dbutils.fs.rm(table_location, recurse=True)

    # Read in the csv file to get the schema
    csv_df = (
        spark.read.format("csv")
        .option("header", "true")
        .option("maxFilesPerTrigger", 1)
        .load(f"file://{sample_data_path}/sample_data.csv")
    )

    # Create the Delta table
    DeltaTable.createIfNotExists(spark).tableName(table_full_name).location(
        table_location
    ).addColumns(csv_df.schema).execute()

    # Read in the csv file as a stream
    csv_stream = (
        spark.readStream.format("csv")
        .schema(csv_df.schema)
        .option("header", "true")
        .option("maxFilesPerTrigger", 1)
        .load(f"file://{sample_data_path}")
    )

    # Write the stream to the delta table
    (
        csv_stream.writeStream.format("delta")
        .option("checkpointLocation", f"{table_location}/checkpoints/")
        .option("mergeSchema", "true")
        .option("outputMode", "complete")
        .table(table_full_name)
    )

    # Job End
    sbnutils.log_info(f"Sample streaming job End")


def _get_job_variables(database_name, table_name, zone_type):
    # Generate full table name
    table_full_name = f"{database_name}.{table_name}"

    # Get Azure storage account location by zone type
    raw_zone_location = sbnutils.get_storage_location(zone_type)

    # Get the location of the delta table
    table_location = f"{raw_zone_location}/{table_name}"
    sbnutils.log_info(f"table_location: {table_location}")

    # Get the path of the sample data csv file
    sample_data_path = os.path.abspath("../sample_data")
    sbnutils.log_info(f"sample_data_path: {sample_data_path}")

    return table_full_name, table_location, sample_data_path
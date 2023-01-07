import os
import yaml

from pyspark.dbutils import DBUtils
from pyspark.sql import SparkSession

class SBNUtils:
    def __init__(self, dbutils: DBUtils):
        self.dbutils = dbutils
        self.spark = SparkSession.builder.getOrCreate()
        env_notebook_mode = os.getenv('NOTEBOOK_MODE')
        self.notebook_mode = env_notebook_mode is not None and env_notebook_mode.lower() == "true"
        if self.notebook_mode:
            self.job_name = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
            self.env = "notebookdev"
        else:
            self.job_name = self.dbutils.widgets.getArgument('job_name')
            self.env = self.dbutils.widgets.getArgument('env')
        
        # Load environment configuration
        with open(f'../config/{self.env}.yaml', 'r') as f:
            self.config = yaml.safe_load(f)
            
        self.log = self.Log(self.spark, self.env, self.job_name)
        self.storage = self.Storage(self.config)
        self.kafka = self.Kafka(self.config, self.dbutils)
        self.database = self.Database()

    class Log:
        def __init__(self, spark, env, job_name):
            self.logger = spark._jvm.org.apache.log4j.Logger.getLogger(f'[{env}]-{job_name}')

        def info(self, message: str):
            self.logger.info(message)

        def error(self, message: str):
            self.logger.error(message)

    class Storage:
        def __init__(self, config):
            self.config = config

        def get_location(self, zone_type: str) -> str:
            return self.config['zone_type'][zone_type]['storage_account_path']

    class Kafka:
        def __init__(self, config, dbutils):
            self.broker = self.Broker(config, dbutils)
            self.schema_registry = self.SchemaRegistry(config, dbutils)

        def get_topic_pattern(self) -> str:
            return self.config['topic_pattern']

        class Broker:
            def __init__(self, config, dbutils):
                self.config = config
                self.dbutils = dbutils

            def get_url(self) -> str:
                return self.config['broker']['url']

            def get_id(self) -> str:
                return self.config['broker']['id']

            def get_secret(self):
                secret_key = self.config['broker']['secret_key']
                secret_scope = self.config['secret_scope']
                return self.dbutils.secrets.get(secret_scope, secret_key)

        class SchemaRegistry:
            def __init__(self, config, dbutils):
                self.config = config
                self.dbutils = dbutils

            def get_url(self) -> str:
                return self.config['schema_registry']['url']

            def get_id(self) -> str:
                return self.config['schema_registry']['id']

            def get_secret(self):
                secret_key = self.config['schema_registry']['secret_key']
                secret_scope = self.config['secret_scope']
                return self.dbutils.secrets.get(secret_scope, secret_key)

    class Database:
        def __init__(self):
            pass

        def get_name(self) -> str:
            return self.config['database']['name']
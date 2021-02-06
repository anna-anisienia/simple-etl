import tempfile
import logging
import boto3
import os
import pandas as pd

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
S3_KEY = 'global_power_plant_database.csv'
S3_BUCKET = 'demo-datasources'


def transform_and_load_to_dwh(filename):
    df = pd.read_csv(filename, nrows=10)
    logger.info(df.info())


with tempfile.TemporaryDirectory() as tmpdir:
    s3 = boto3.client('s3')
    local_file_path = os.path.join(tmpdir, S3_KEY)
    s3.download_file(S3_BUCKET, S3_KEY, local_file_path)
    transform_and_load_to_dwh(local_file_path)

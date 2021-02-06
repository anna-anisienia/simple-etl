from pathlib import Path
import shutil
import logging
import boto3
import os
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
S3_KEY = 'global_power_plant_database.csv'
S3_BUCKET = 'demo-datasources'
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
local_path = os.path.join(ROOT_DIR, 'data')
local_file_path = os.path.join(local_path, S3_KEY)


def transform_and_load_to_dwh(filename):
    df = pd.read_csv(filename, nrows=10)
    logger.info(df.info())


Path(local_path).mkdir(parents=True, exist_ok=True)
s3 = boto3.client('s3')
s3.download_file(S3_BUCKET, S3_KEY, local_file_path)
transform_and_load_to_dwh(local_file_path)
shutil.rmtree(local_path, ignore_errors=False)

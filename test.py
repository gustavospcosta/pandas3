import os
import pandas as pd
from google.cloud import storage
from sqlalchemy import create_engine
import numpy as np

def download_dataset():
    """
    Downloads the New York City Airbnb open data from Kaggle.
    """
    od.download("https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data")

def authenticate_gcloud(path):
    """
    Authenticates with Google Cloud using the provided JSON path.

    Args:
        path (str): Path to the JSON file containing the authentication credentials.

    Returns:
        google.cloud.storage.client.Client: Authenticated Google Cloud storage client.
    """
    return storage.Client.from_service_account_json(path)

def select_bucket(client, bucket_name):
    """
    Selects the specified bucket from Google Cloud Storage.

    Args:
        client (google.cloud.storage.client.Client): Authenticated Google Cloud storage client.
        bucket_name (str): Name of the bucket to select.

    Returns:
        google.cloud.storage.bucket.Bucket: Selected Google Cloud Storage bucket.
    """
    return client.get_bucket(bucket_name)

def b_upload(blob_name, fp_upload, bucket):
    """
    Uploads a file to a Google Cloud Storage bucket.

    Args:
        blob_name (str): The name of the blob (file) to upload.
        fp_upload (str): The local file path of the file to upload.
        bucket (google.cloud.storage.bucket.Bucket): Target Google Cloud Storage bucket.

    Returns:
        bool: True if upload was successful, False otherwise.
    """
    try:
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(fp_upload)
        print(f'FILE UPLOADED!')
        return True
    except Exception as error_up:
        print(f'ERROR WHILE UPLOADING FILE: {error_up}')
        return False

def b_download(blob_name, fp_download, bucket):
    """
    Downloads a file from a Google Cloud Storage bucket.

    Args:
        blob_name (str): The name of the blob (file) to download.
        fp_download (str): The local file path to save the downloaded file.
        bucket (google.cloud.storage.bucket.Bucket): Source Google Cloud Storage bucket.

    Returns:
        bool: True if download was successful, False otherwise.
    """
    try:
        blob = bucket.blob(blob_name)
        with open(fp_download, "wb") as s_arquivo:
            storage_client.download_blob_to_file(blob, s_arquivo)
            print(f'FILE DOWNLOADED!')
        return True
    except Exception as error_down:
        print(f'ERROR WHILE DOWNLOADING FILE: {error_down}')
        return False

def read_and_preprocess_data(dataset_url):
    """
    Reads and preprocesses the dataset from the given URL.

    Args:
        dataset_url (str): URL to the dataset.

    Returns:
        pd.DataFrame: Processed dataset.
    """
    data_set = pd.read_csv(dataset_url, engine='python', quoting=3, verbose=True, encoding='utf-8-sig')
    data_set = data_set.replace('*', '|', regex=True)
    return data_set

def replace_nan_values(df):
    """
    Replaces NaN values in the given DataFrame with specific values.

    Args:
        df (pd.DataFrame): The DataFrame with NaN values to be replaced.

    Returns:
        pd.DataFrame: DataFrame with NaN values replaced.
    """
    nan_replacements = {'id': 0, 'host_id': 0, 'latitude': 0, 'longitude': 0, 'price': 0,
                        'minimum_nights': 0, 'number_of_reviews': 0, 'last_review': "1111-11-11",
                        'reviews_per_month': 0, 'calculated_host_listings_count': 0, 'availability_365': 0}
    df = df.fillna(nan_replacements)
    return df

def save_to_mysql(df, connection_string):
    """
    Saves the given DataFrame to a MySQL database using the provided connection string.

    Args:
        df (pd.DataFrame): The DataFrame to be saved.
        connection_string (str): Connection string for the MySQL database.

    Returns:
        None
    """
    engine = create_engine(connection_string)
    df.to_sql('AIRBNB', con=engine, if_exists='append', index=False)

# MAIN EXECUTION #
path_upload = r"/YOUR/PATH/YOUR_FOLDER/"
f_path_upload = os.path.join(path_upload, "AB_NYC_2019.csv")
path_download = r"G:\YOUR\FOLDER"
f_path_download = os.path.join(path_download, "data_teste.csv")
bucket_name = 'YOUR_BUCKET_NAME'

download_dataset()
storage_client = authenticate_gcloud("/YOUR/PATH/FILE.json")
bucket = select_bucket(storage_client, bucket_name)

b_upload("YOUR_FOLDER/data_airbnb_ny_2019", f_path_upload, bucket)
b_download("YOUR_FOLDER/data_airbnb_ny_2019", f_path_download, bucket)

data_set = read_and_preprocess_data(dataset_url)
data_set = replace_nan_values(data_set)

connection_string = "mysql+pymysql://USER:PASSWORD@LOCALHOST:PORT/DBNAME"
save_to_mysql(data_set, connection_string)

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

from config import connect_str, container_name


def get_blob_client(file):
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file)
    return blob_client

# Upload the file
def upload(file):
    blob_client = get_blob_client(file)
    with open(file, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

# Download the file
def download(file):
    blob_client = get_blob_client(file)
    with open(file, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

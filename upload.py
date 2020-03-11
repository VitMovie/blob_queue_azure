from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

from config import connect_str, container_name


# Upload the file
def upload(file):
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file)
    with open(file, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
import os

account_name = os.getenv("STORAGE_ACCOUNT_NAME")
account_key = os.getenv("STORAGE_ACCOUNT_KEY")
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = os.getenv("BLOB_CONTAINER_NAME")
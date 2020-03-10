import glob, time
from itertools import cycle

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.storage.queue import QueueService

from config import connect_str, container_name, account_name, account_key

# Upload the file
def upload(file):
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file)
    with open(file, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

# Send new user to leaderboard
def send_new_user():
    queue_service = QueueService(account_name=account_name, account_key=account_key)
    queue_service.create_queue('newuser')
    queue_service.put_message('newuser', f'user_{int(time.time())}')


files = glob.glob('./data/*.txt', recursive=True)
for file in cycle(files):
    upload('followers.txt') # upload and update followers list
    upload(file)
    send_new_user()
    time.sleep(10)


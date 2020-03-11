import glob, time

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.storage.queue import QueueService

from config import account_name, account_key


# Send new user to leaderboard
def send_new_user():
    queue_service = QueueService(account_name=account_name, account_key=account_key)
    queue_service.create_queue('newuser')
    queue_service.put_message('newuser', f'user_{int(time.time())}')

def recognition():
    while True:
        send_new_user()
        time.sleep(10)


recognition()

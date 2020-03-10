import time

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.storage.queue import QueueService

from config import account_name, account_key


def add_new_user(new_user):
    with open("followers.txt", "a") as file:
        file.write(f"{new_user}\n")

def counting():
    queue_service = QueueService(account_name=account_name, account_key=account_key)
    while True:
        messages = queue_service.get_messages('newuser')
        if messages:
            for message in messages:
                add_new_user(message.content)
                queue_service.delete_message('newuser', message.id, message.pop_receipt)
        time.sleep(30)

counting()
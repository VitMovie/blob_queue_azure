import time

from azure.storage.queue import QueueService

from config import account_name, account_key
from load import upload
from delivery import get_new_proxy


def add_new_user(new_user):
    with open("followers.txt", "a") as file:
        file.write(f"{new_user}\n")
    upload("followers.txt")

def counting():
    queue_service = QueueService(account_name=account_name, account_key=account_key)
    while True:
        messages = queue_service.get_messages('newuser')
        if messages:
            for message in messages:
                add_new_user(message.content)
                queue_service.delete_message('newuser', message.id, message.pop_receipt)
        print(get_new_proxy())
        time.sleep(30)


counting()

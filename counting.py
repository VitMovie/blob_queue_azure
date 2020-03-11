import time

from azure.storage.queue import QueueService

from config import account_name, account_key
from load import upload
from delivery import get_new_proxy


def add_new_user(new_user):
    with open("followers.txt", "a") as file:
        print(f"Adding {new_user} to followers.txt...")
        file.write(f"{new_user}\n")
    print("Uploading followers.txt to blob storage")
    upload("followers.txt")

def counting():
    queue_service = QueueService(account_name=account_name, account_key=account_key)
    while True:
        messages = queue_service.get_messages('newuser')
        if messages:
            for message in messages:
                print(f"Receiving {new_user} from newuser channel...")
                add_new_user(message.content)
                print(f"Deleteing {new_user} from queue of users...")
                queue_service.delete_message('newuser', message.id, message.pop_receipt)
        new_proxy = get_new_proxy()
        print(f"Receiving proxy {new_proxy} from queue of proxies...")
        time.sleep(30)


counting()

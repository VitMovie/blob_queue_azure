import time
from azure.storage.queue import QueueService

from config import account_name, account_key


def scrapping():
    queue_service = QueueService(account_name=account_name, account_key=account_key)
    while True:
        messages = queue_service.get_messages('monitoring')
        if messages:
            for message in messages:
                print(message.content)
                queue_service.delete_message('monitoring', message.id, message.pop_receipt)
        time.sleep(30)

scrapping()
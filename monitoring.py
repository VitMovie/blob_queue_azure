import time
from azure.storage.queue import QueueService

from config import account_name, account_key


def check():
    queue_service = QueueService(account_name=account_name, account_key=account_key)
    queue_service.create_queue('monitoring')
    while True:
        queue_service.put_message('monitoring', f'monitoring_{int(time.time())}')
        time.sleep(10)

check()
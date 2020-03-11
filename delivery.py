import time

from azure.storage.queue import QueueService

from config import account_name, account_key
from load import download


def get_proxies():
    download("proxies.txt")
    with open("proxies.txt", "r") as file:
        proxies = [line.strip() for line in file.readlines()]
    return proxies

def create_queue_of_proxies(proxies):
    queue_service = QueueService(account_name=account_name, account_key=account_key)
    queue_service.create_queue('proxies')
    for proxy in proxies:
        queue_service.put_message('proxies', proxy)

def get_new_proxy():
    queue_service = QueueService(account_name=account_name, account_key=account_key)
    messages = queue_service.get_messages('proxies')
    if messages:
        for message in messages:
            new_proxy = message.content
            queue_service.delete_message('proxies', message.id, message.pop_receipt)
        queue_service.put_message('proxies', new_proxy)
    return new_proxy


proxies = get_proxies()
create_queue_of_proxies(proxies)

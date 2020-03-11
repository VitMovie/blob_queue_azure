import glob, time
from itertools import cycle

from load import upload


def send_photos():
    files = glob.glob('./data/*.txt', recursive=True)
    for file in cycle(files):
        print(f"Uploading {file} to blob storage...")
        upload(file)
        time.sleep(10)

send_photos()

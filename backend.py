import glob, time
from itertools import cycle

from load import upload


def send_photos():
    files = glob.glob('./data/*.txt', recursive=True)
    for file in cycle(files):
        upload(file)
        time.sleep(10)

send_photos()

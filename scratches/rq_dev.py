import requests
from redis import Redis
from rq import Queue

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())

redis_connection = Redis()

q = Queue(connection=redis_connectionm,is_async=True,)

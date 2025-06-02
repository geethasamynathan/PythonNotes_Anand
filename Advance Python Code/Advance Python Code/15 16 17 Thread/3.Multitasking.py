import threading
import requests

def fetch_url(url):
    response = requests.get(url)
    print(f"Fetched {url} with {len(response.content)} bytes.")

urls = [
    "https://www.pythontutorial.net/",
    "https://pandas.pydata.org/",
    "https://www.djangoproject.com/"
]    

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))  # Fixed args
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('All URLs Fetched')

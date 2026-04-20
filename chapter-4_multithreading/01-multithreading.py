import time
from concurrent.futures import ThreadPoolExecutor
def fetch_response(url:str):
    print(f"Fetching Data from {url}")
    time.sleep(3)
    print(f"✔ Done")
    return f"✔ Fetch data successfully from {url}"

url_list = ["https://url_1.com",
            "https://url_2.com",
            "https://url_3.com",
            "https://url_4.com"]

res = []
with ThreadPoolExecutor(max_workers=(len(url_list))) as executor:
    futures = executor.map(fetch_response,url_list)
    res.extend(futures)

print(res)
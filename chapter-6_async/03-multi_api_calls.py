import asyncio
from random import random

async def api_call(url, delay):
    print(f"Wait {delay} seconds from {url} ...")
    await asyncio.sleep(delay)
    print(f"Fetched Data from {url}")
    return f" < {url} Data >"

async def executer():
    urls = ["url_1" , "url_2" , "url_3"]
    tasks = [api_call(url,4 - (urls.index(url) + 1)) for url in urls] #Creating a list of tasks for each API call with different URLs and the same delay
    results = await asyncio.gather(*tasks)
    print(f"✔ Sucessfully fetched all data")

asyncio.run(executer())
    
    
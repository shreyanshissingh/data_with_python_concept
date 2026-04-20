import asyncio

async def api_call_orders():
    await asyncio.sleep(3)
    return f" < Orders Data >"

async def executer():
    print("Executing API Call ...")
    res = await api_call_orders() #Async makes thread available for other tasks 
    print(f"✔ Sucessfully fetched {res}")

asyncio.run(executer())
    
    
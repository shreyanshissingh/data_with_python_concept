import asyncio
import time

def main():   #This one locks the thread, means processor is not free to perform other tasks
    print("Hello")
    time.sleep(3)
    print("World")

async def main_1():  #This is not lock the thread
    print("Hello")
    await asyncio.sleep(3) #Without await it will not wait for 3 seconds and will print "World" immediately after "Hello"
    print("World") #Even if we use await, it will not block the thread, it will allow other tasks to run while waiting for the sleep to complete

main()
asyncio.run(main_1())
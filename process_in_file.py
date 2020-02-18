import asyncio
from aiomultiprocess import Process, Worker
import aiomultiprocess
import os

aiomultiprocess.set_start_method('fork')

async def do_sleep():
    while True:
        print(os.getpid())
        await asyncio.sleep(1)

async def create_process():
    p = Process(target=do_sleep)
    p.start()
    #import pdb; pdb.set_trace()
    # p.terminate() # here works
    return p

async def main():
    p = await create_process()
    #p.terminate()
    
if __name__ == "__main__":
    asyncio.run(main())

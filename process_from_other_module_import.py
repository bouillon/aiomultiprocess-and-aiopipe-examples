import asyncio
import os


async def do_sleep():
    while True:
        print(os.getpid())
        await asyncio.sleep(1)


# import aiomultiprocess
# aiomultiprocess.set_start_method('fork')
# from aiomultiprocess import Process, Worker
# async def create_process():
#     p = Process(target=do_sleep)
#     p.start()
#     p.join

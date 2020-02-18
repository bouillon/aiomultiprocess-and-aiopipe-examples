import os
import asyncio
from aiomultiprocess import Process, Worker
import aiomultiprocess
import process_from_other_module_import

aiomultiprocess.set_start_method('fork')

async def create_process():
    p = Process(target=process_from_other_module_import.do_sleep)
    return await p

async def main():
    p = await create_process()
    
if __name__ == "__main__":
    asyncio.run(main())

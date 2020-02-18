import asyncio
from aiomultiprocess import Process
from aiopipe import aioduplex
import aiomultiprocess
import json

aiomultiprocess.set_start_method('fork')

async def test(ipc):
    async with ipc.open() as (rx, tx):
        tx.write(json.dumps({'a':1, 'b':2}).encode())
        rep = await rx.readline()
        tx.write(rep)

async def main():
    mainpipe, chpipe = aioduplex()
    with chpipe.detach() as chpipe:
        proc = Process(target=test, args=(chpipe,))
        proc.start()

    async with mainpipe.open() as (rx, tx):
        req = await rx.read(100)
        #tx.write(req + b" world\n")
        print(req)
        print('1')
        tx.write(req + b"\n")
        print('2')
        msg = await rx.readline()
    
    await proc.join()
    print(msg)

if __name__ == "__main__":
    asyncio.run(main())

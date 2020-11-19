import asyncio
import logging
from aiohttp import web

logging.basicConfig(level=logging.INFO)

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', headers={'content-type': 'text/html'})

async def init():
    app = web.Application()
    app.router.add_route('GET', '/', index)
    runner = web.AppRunner(app=app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 9000)
    await site.start()
    logging.info('server started at http://127.0.0.1:9000...')
    return site

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()
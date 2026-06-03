from aiohttp import web

async def web_server():
    app = web.Application()
    return app

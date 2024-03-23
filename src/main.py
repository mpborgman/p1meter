import asyncio
import reader
import aiopg

from aiohttp import web

app_config = {
    "store": True,
    "DB_HOST": "rpibrain.borgmannen.org",
    "DB_PORT": 5432,
    "DB_DATABASE": "p1meter",
    "DB_USER": "admin",
    "DB_PASS": "WN8!|-42Br"
}


async def handler(request):
    return web.json_response(request.app["p1telegram"])


async def create_p1reader(app):
    app['p1reader'] = asyncio.create_task(reader.retrieve(app))


async def close_p1reader(app):
    app['p1reader'].cancel()
    await app['p1reader']


async def create_pg_engine(app):
    app['pg_pool'] = await aiopg.create_pool(
        host=app_config['DB_HOST'],
        port=app_config['DB_PORT'],
        dbname=app_config['DB_DATABASE'],
        user=app_config['DB_USER'],
        password=app_config['DB_PASS']
    )


async def close_pg_engine(app):
    app['pg_pool'].close()
    await app['pg_pool'].closed()


# async def p1reader_web_app():
app = web.Application()
app.add_routes([web.get('/', handler)])
if app_config["store"]:
    app.on_startup.append(create_pg_engine)
    app.on_cleanup.append(close_pg_engine)
app.on_startup.append(create_p1reader)
app.on_cleanup.append(close_p1reader)
web.run_app(app)

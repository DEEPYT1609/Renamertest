from flask import Flask
from time import sleep, time
from psutil import boot_time, disk_usage, net_io_counters
from subprocess import check_output
from os import path as ospath
app = Flask(__name__)
botStartTime = time()
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("LazyDeveloper")

@route.get('/status', allow_head=True)
async def status(request):
    return web.json_response("uptime": time() - boot_time(),"on_time": time() - botStartTime,"free_disk": disk_usage('.').free,"total_disk": disk_usage('.').total,"network": {"sent": net_io_counters().bytes_sent,"recv": net_io_counters().bytes_recv})


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

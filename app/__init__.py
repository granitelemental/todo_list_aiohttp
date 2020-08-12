from aiohttp import web
from asyncio import get_event_loop

from .views import IndexView, TaskView

import config


loop = get_event_loop()

app = web.Application(loop=loop)

index_resource = app.router.add_resource('/', name='index')
is_done_filter_resource = app.router.add_resource('/{is_done}', name='is_done_filter')
task_resource = app.router.add_resource('/task/{uuid}', name='task')

index_resource.add_route("GET", IndexView.get)
index_resource.add_route("POST", IndexView.post)
index_resource.add_route("DELETE", IndexView.delete)

is_done_filter_resource.add_route("GET", IndexView.get)

task_resource.add_route("GET", TaskView.get)
task_resource.add_route("PATCH", TaskView.patch)
task_resource.add_route("DELETE", TaskView.delete)

web.run_app(app, host=config.HOST, port=config.PORT)

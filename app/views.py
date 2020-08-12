
from aiohttp.web import Response, json_response, View, Request

from .models import Task


class IndexView:

    async def get(request):
        tasks = Task.get_all_tasks()
        return json_response(tasks)

    async def get(request):
        is_done = request.match_info.get('is_done')
        tasks = Task.get_all_tasks(is_done)
        return json_response(tasks)

    async def delete(request):
        Task.delete_all_tasks()
        return Response()

    async def post(request):
        data = await request.json()
        task = Task.create_task(data.get("name"), \
            data.get("date_created"))
        return json_response(task)


class TaskView:

    async def get(request):
        uuid = request.match_info.get('uuid')
        task = Task.get_task(uuid)
        return json_response(task)

    async def patch(request):
        data = await request.json()
        uuid = request.match_info.get('uuid')
        task = Task.update_task(uuid, data)
        return json_response(task)
    
    async def delete(request):
        uuid = request.match_info.get('uuid')
        Task.delete_task(uuid)
        return Response()

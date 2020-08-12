
from aiohttp.web import Response, json_response

from .models import Task


class IndexView:

    @classmethod
    async def get(cls, request):
        try:
            status = request.rel_url.query['status']
        except:
            status = None
        tasks = Task.get_all_tasks(status)
        return json_response(tasks)

    @classmethod
    async def delete(cls, request):
        Task.delete_all_tasks()
        return Response()

    @classmethod
    async def post(cls, request):
        data = await request.json()
        task = Task.create_task(data.get("name"), \
            data.get("date_created"))
        return json_response(task)


class TaskView:

    @classmethod
    async def get(cls, request):
        uuid = request.match_info.get('uuid')
        task = Task.get_task(uuid)
        return json_response(task)

    @classmethod
    async def patch(cls, request):
        data = await request.json()
        uuid = request.match_info.get('uuid')
        task = Task.update_task(uuid, data)
        return json_response(task)

    @classmethod
    async def delete(cls, request):
        uuid = request.match_info.get('uuid')
        Task.delete_task(uuid)
        return Response()

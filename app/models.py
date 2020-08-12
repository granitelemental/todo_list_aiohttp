from glob import glob
from json import dump, load

from uuid import uuid4

import config


db_path = config.DB_PATH


class Task:
    
    if glob(db_path):
        with open(db_path, "r") as f:
            tasks = load(f)
    else:
        tasks = {}

    @classmethod
    def sync_db(cls):
        with open(db_path, "w") as f:
            dump(cls.tasks, f, indent=4, ensure_ascii=False)

    @classmethod
    def create_task(cls, name, date_created):
        uuid = str(uuid4())
        task = {
            "uuid": uuid,
            "date_created": date_created,
            "name": name,
            "status": "active"
        }
        cls.tasks.update({uuid: task})
        cls.sync_db()
        return task

    @classmethod
    def delete_task(cls, uuid):
        del cls.tasks[uuid]
        cls.sync_db()

    @classmethod
    def update_task(cls, uuid, data):
        cls.tasks[uuid].update(data)
        cls.sync_db()
        return cls.tasks[uuid]

    @classmethod
    def get_task(cls, uuid):
        cls.sync_db()
        return cls.tasks[uuid]

    @classmethod
    def get_all_tasks(cls, status=None):
        if cls.tasks and (status is not None):
            print(">", status)

            tasks = {
                uuid: task for uuid, task in cls.tasks.items() \
                     if task["status"] == status
            }
            return tasks
        else:
            return cls.tasks

    @classmethod
    def delete_all_tasks(cls):
        cls.tasks = {}
        cls.sync_db()

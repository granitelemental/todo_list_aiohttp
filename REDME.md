## 1) Backend start:
```
pip install -r requirements.txt
python runserver.py
```
## 2) Requests to api:

- `POST /` - If database does not exist creates file `db.json` and stores task in it. If `db.json` exists updates it with posted task.  Request body format: 
```
{
	"name": "Do something",
	"date_created": 1234566 # timestamp
}
```
Response example:
```
{
  "uuid": "3f05f10f-0071-44ec-8eac-e9b53374f18a",
  "date_created": 123,
  "name": "Do something",
  "done": false
}
```

- `GET /` - gets json with all tasks. Response example:
```
{
  "6aacac0d-d507-4ee6-ab81-e833635e6658": {
    "uuid": "6aacac0d-d507-4ee6-ab81-e833635e6658",
    "date_created": 123,
    "name": "the bestest task",
    "done": false
  },
  "3f05f10f-0071-44ec-8eac-e9b53374f18a": {
    "uuid": "3f05f10f-0071-44ec-8eac-e9b53374f18a",
    "date_created": 123,
    "name": "Do something",
    "done": false
  }
}
```

- `GET /{is_done}` - returns json with all active tasks if `is_done = active`, and json with all done tasks if `is_done = done`. 

- `DELETE /` - clear database.

- `GET /task/{uuid}` - returns the task with the `uuid`.  Response example:
```
{
  "uuid": "6aacac0d-d507-4ee6-ab81-e833635e6658",
  "date_created": 123,
  "name": "Do something",
  "done": false
}
```

- `PATCH /task/{uuid}` - updates the task with the `uuid`.  Request body example:
```
{
	"name": "Do something else", 
    "done": true
}
```

Response example:
```
{
  "uuid": "6aacac0d-d507-4ee6-ab81-e833635e6658",
  "date_created": 123,
  "name": "Do something else",
  "done": true
}
```

- `DELETE /task/{uuid}` - deletes the task with the `uuid`.

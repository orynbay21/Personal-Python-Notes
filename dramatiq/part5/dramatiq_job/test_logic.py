
"""
import time
from main import factorial, send_request_to_our_server, result_backend
task=send_requst_to_our_server.send()
time.sleep(5)
result=result_backend.get_result(task)
print(result)
"""


import time

from pydantic import BaseModel
from fastapi import FastAPI
from dramatiq.results.errors import ResultMissing

from main import factorial, send_request_to_our_server, result_backend

app = FastAPI()


class Employee(BaseModel):
    name: str
    age: int


@app.post("/add_employee")
def add_employee(employee: Employee):
    task = send_request_to_our_server.send(employee.name)
    return {'id': task.message_id}


@app.get("/result")
def result(id: str):
    try:
        task = send_request_to_our_server.message().copy(message_id=id)
        return result_backend.get_result(task)
    except ResultMissing:
        return "Waiting for all requests"
#uvicorn test_logic:app --reload --port 9000



"""
in order to run this part 5
at dramatiq_job/main.py start dramatiq main
at dramatiq_job/test_logic start uvicorn test_logic:app --reload --port 9000
at test_server/main.py terminal start uvicorn main:app --reload

"""
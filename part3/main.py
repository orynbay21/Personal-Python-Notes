from fastapi import FastAPI
import requests
import dramatiq
from requests import ReadTimeout
app=FastAPI()

@app.get('/')
def test():
    return {"hie":"hello"}

def when_to_retry(num_of_retries:int,exc:Exception)->bool:
    if isinstance(exc,ReadTimeout):
        return True
    return False

@dramatiq.actor
def send_request_to_our_server(retry_when=when_to_retry):
    response=requests.get('http://127.0.0.1:8000',timeout=5)
    print(response.json())

"""
in order to run this

1) restart docker image
2) write dramatiq main
3)uvicorn main:app --reload
4)py test.py
"""
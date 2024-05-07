from fastapi import FastAPI
import requests
import dramatiq
app=FastAPI()

@app.get('/')
def test():
    return {"hie":"hello"}

@dramatiq.actor
def send_request_to_our_server():
    response=requests.get('http://127.0.0.1:8000')
    print(response.json())

"""
in order to run this

1) restart docker image
2) write dramatiq main
3)uvicorn main:app --reload
4)py test.py
"""
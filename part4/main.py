from fastapi import FastAPI
import requests
import dramatiq
import random
from requests import ReadTimeout
app=FastAPI()

def test(name:str):
    return not name=='Arslan'


@app.get("/drug")
def drug_endpoint(name:str):
    return test(name)


@app.get("/psycho")
def psycho_endpoint(name:str):
    return test(name)

@app.get("/crime")
def crime_endpoint(name:str):
    return test(name)

def when_to_retry(num_of_retries:int,exc:Exception)->bool:
    if isinstance(exc,ReadTimeout):
        return True
    return False


"""
in order to run this

1) restart docker image
2) write dramatiq main
3)uvicorn main:app --reload
4)py test.py
"""
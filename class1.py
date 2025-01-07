# from fastapi import FastAPI
# import requests


# app = FastAPI()

# @app.route('/')
# def hello():
#     return {'message': 'hello'}


from typing import List

#type hinting
#type hinted function
def fun(x: str) -> str:
    return x.capitalize()

my_fun = fun('hi')
print(my_fun)


def fun2(a: List[float]) -> str:
    return a[1]

my_list = [1.2, 3.4, 5.7]

a = fun2(my_list)
print(a)


#pydantic
from pydantic import BaseModel

#ngnix for https

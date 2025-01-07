from fastapi import Body, FastAPI, Response, status
from pydantic import BaseModel

app = FastAPI()

class CreatePostIn(BaseModel):
    title: str
    content: str


# @app.get('/{id}', status_code=status.HTTP_200_OK)
# def home_page(id:int, response:Response):
#     if id > 6:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return 'error'
#     return 'hello'


@app.post('/create')
async def create_post(post: CreatePostIn = Body()):
    return post




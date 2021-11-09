from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {"item_id": 5, "q": "somequery", 'data':{'name':'ruhul', 'id':'Sonar Bangladesh'}}

@app.get('/about')
def about():
    return {'page_name': 'about', 'content': 'Lorem Ipsum'}

@app.get('/blog')
def blog(limit=10, offset:Optional[int]=0):
    return {'page_name': 'blog', 'content': 'Lorem Ipsum', 'limit': limit, 'offset': offset}

@app.get('/blog/{id}')
def blog(id: int):
    return {'page_name': 'blod', 'id': id}

class Blog(BaseModel):
    title: str
    body: str
    status: Optional[bool]=True

@app.post('/blog/create')
def blog(request: Blog):
    return {'page_name': 'Create blog', 'blog title': request.title}

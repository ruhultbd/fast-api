from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"item_id": 5, "q": "somequery", 'data':{'name':'ruhul', 'id':'Sonar Bangladesh'}}

@app.get('/about')
def about():
    return {'page_name': 'about', 'content': 'Lorem Ipsum'}

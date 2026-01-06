import datetime

from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status

app = FastAPI()
fake_db = [
    {"title": "Criando uma aplicacação com Django", "date": datetime.date.today(), "published": True },
    {"title": "Criando uma aplicacao com FastAPI", "date": datetime.date.today(), "published": True },
    {"title": "Criando uma aplicacao com Flask", "date": datetime.date.today(), "published": True },
    {"title": "Criando uma aplicacao com Stalett", "date": datetime.date.today(), "published": False }
]

class Post(BaseModel):
    title: str
    date: datetime.date = datetime.date.today()
    published: bool = False
    author: str

@app.post("/posts/", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    fake_db.append(post.model_dump())
    return post

#QUERY PARAMETERS-------------------------------
#@app.get("/posts")
#def read_posts(skip: int = 0, limit: int = len(fake_db)):
#    return fake_db[skip:skip + limit]
@app.get("/posts/")
def read_posts(published: bool,skip: int = 0, limit: int = len(fake_db)):
    return [post for post in fake_db[skip:limit] if post["published"] is published]

#@app.get("/posts")
#def read_posts(skip: int = 0, limit: int = len(fake_db)):
    return fake_db[skip:skip + limit]
#QUERY PARAMETERS-------------------------------
@app.get("/")
def read_root():
    return {"message": "Hello World!!!"}

@app.get("/posts/{framework}")
def read_post(framework: str):
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}!", "date": datetime.datetime.now(datetime.UTC)},
            {"title": f"Internacionalizando um app {framework}!", "date": datetime.datetime.now(datetime.UTC)},
        ]
    }
#Parei em Rotas e endpoints em FastAPI - Path parameter
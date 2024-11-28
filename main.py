from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

@app.get("/")
def read_root():
    return {"Hello": "Welcome to my API and practicals"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your post."}


@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    return {"data": "new post"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Welcome to my API and practicals"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your post."}
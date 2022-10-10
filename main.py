
from fastapi import FastAPI
import models, posts, user, auth
from database import engine
import posts, auth, vote
from config import settings
from fastapi.middleware.cors import CORSMiddleware

#models.Base.metadata.create_all(bind=engine)
# some text

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

my_posts = [{"title": "title of the post 1", "content": "content of post 1", "id" : 1}, {"title": "favorite foods", "content": "i like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

app.include_router(posts.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Hello World, it is great"}






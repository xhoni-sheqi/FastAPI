from fastapi import FastAPI , HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
# calling app is a convention
app = FastAPI()


# extends basemodel 
# check typo 
# check alll of the validation and design the schema 
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


# save post [ no db ]

my_posts = []
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
    return None

#decorate
@app.get("/")
#plain python function - name the function as descriptive as possible
def root():
    return {"message": "Hello World"} 

 
@app.get("/posts")
def get_posts():
    return {"data": my_posts} 

@app.post("/posts")
# auto extract the content
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,9999999)
    my_posts.append(post_dict) 
    return {"data" : post_dict}


@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(int(id))
    return {"post": post}

# title -> str and content -> str , we can include wherether we want 
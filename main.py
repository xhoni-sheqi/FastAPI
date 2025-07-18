from fastapi import FastAPI , Response , status , HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
# calling app is a convention
# CRUD API
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

# array to save ( db is a better choice indeed )
my_posts = []
#search for a single post by id
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
    return None

#decorate - health check in the root 
@app.get("/")
#plain python function - name the function as descriptive as possible
def root():
    return {"message": "Hello World"} 

 
# get all post 

@app.get("/posts")
def get_posts():
    return {"data": my_posts} 

# post a post

@app.post("/posts")
# auto extract the content
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,9999999)
    my_posts.append(post_dict) 
    return {"data" : post_dict}

# get a single post 

@app.get("/posts/{id}")
def get_post(id: int ,response: Response):
    post = find_post(id)
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message' : f"post with id {id} was not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    return {"post": post}

# title -> str and content -> str , we can include wherether we want 
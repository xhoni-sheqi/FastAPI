from fastapi import FastAPI 
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

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

#decorate
@app.get("/")
#plain python function - name the function as descriptive as possible
def root():
    return {"message": "Hello World"} 

 
@app.get("/posts")
def get_posts():
    return {"data": "First Post"} 

@app.post("/createposts")
# auto extract the content
def create_post(post: Post): 
    print(post)
    # you can use .dict() 
    print(post.dict())
    return {"message": "Post created" , "new_post": post}


# title -> str and content -> str , we can include wherether we want 
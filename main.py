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

@app.post("/createpost")
# auto extract the content
def create_post(new_post: Post): 
    print(new_post)
    # you can use .dict() 
    print(new_post.dict())
    return {"message": "Post created" , "new_post": new_post}


# title -> str and content -> str , we can include wherether we want 
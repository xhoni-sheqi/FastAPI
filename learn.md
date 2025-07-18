virtaul env that will not affect other env and will not install package everywhere but only in the venv
create a venv : py -3 -m venv venv
view -> command palette -> select enterpreter -> python v.n venv
venv\Scripts\activate

install fastAPI 
pip install fastapi[all]
uvicorn -> webserver

run the web server : 
uvicorn main(name of the file.py):app


from fastapi import FastAPI 

# calling app is a convention
app = FastAPI()
#decorate
@app.get("/")
#plain python function - name the function as descriptive as possible
def root():
    return {"message": "Hello World"} 

@ -> makes it a decorator | make it possible to be an API  
app -> ref to our app 
get -> you can perform all of http methods 
("/") -> paths 
@app.get("/")

if we have the same route the order metters

https://www.itransition.com/careers/python-junior-developer

@app.post("/createpost")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"message": "success"}
Get the body 

but we need to fix : 

it's a pain to get all the values from the body 
the client can send whatever data they want
the data isn't getting validated 
we ultimately want to force the client to send data in schema that we expect 

for this we use pydentic

from pydantic import BaseModel
from typing import Optional


# extends basemodel 
# check typo 
# check alll of the validation and design the schema 
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None



@app.post("/createposts")
# auto extract the content
def create_post(post: Post): 
    print(post)
    # you can use .dict() 
    print(post.dict())
    return {"message": "Post created" , "new_post": post}


# title -> str and content -> str , we can include wherether we want 

use always plural name when refereng the routes 
retrive data -> get 
post data -> post 
retrive specific data -> get
upddate some data -> put/patch
delete some data -> delete

# when working with api use top down approach and remember ORDER COUNTS 


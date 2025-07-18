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
my_posts = [{"title": "a", "content": "b", "published" : True , "rating":123, "id" : 1},{"title": "a", "content": "b", "published" : True , "rating": 12, "id" : 2}]
#search for a single post by id
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
    return None

def find_index_post(id):
    for i,post in enumerate(my_posts):
        if post['id'] == id:
            return i
    return None

#decorate - health check in the root 
@app.get("/")
#plain python function - name the function as descriptive as possible
def root():
    return {"message": "Hello World"} 

 
# get all post - 200 is for get and put

@app.get("/posts")
def get_posts():
    return {"data": my_posts} 

# post a post - 201 is for post op

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

# delete  - 204 is for delete op

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    #deleting post
    # find the index in the array required ID
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} doesn't exist ")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} doesn't exist ")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}

# title -> str and content -> str , we can include wherether we want 
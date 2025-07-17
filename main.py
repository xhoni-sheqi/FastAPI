from fastapi import FastAPI 
from fastapi.params import Body

# calling app is a convention
app = FastAPI()
#decorate
@app.get("/")
#plain python function - name the function as descriptive as possible
def root():
    return {"message": "Hello World"} 

 
@app.get("/posts")
def get_posts():
    return {"data": "First Post"} 

@app.post("/createpost")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"message": "success"}
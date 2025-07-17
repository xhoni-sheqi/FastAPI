from fastapi import FastAPI 

# calling app is a convention
app = FastAPI()
#decorate
@app.get("/")
#plain python function - name the function as descriptive as possible
def root():
    return {"message": "Hello World"} 
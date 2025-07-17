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
virtaul env that will not affect other env and will not install package everywhere but only in the venv
create a venv : py -3 -m venv venv
view -> command palette -> select enterpreter -> python v.n venv
venv\Scripts\activate

install fastAPI 
pip install fastapi[all]
uvicorn -> webserver
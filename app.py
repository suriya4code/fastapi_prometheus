from fastapi import FastAPI
from prometheus_client import make_asgi_app

# Create app
app = FastAPI(debug=False)

# Add prometheus asgi middleware to route /metrics requests
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)



@app.get("/")
def root():
    return "todooo"

@app.post("/todo")
def create_todo():
    return "create todo item"

@app.get("/todo/{id}")
def read_todo(id: int):
    return "read todo item with id {id}"

@app.put("/todo/{id}")
def update_todo(id: int):
    return "update todo item with id {id}"

@app.delete("/todo/{id}")
def delete_todo(id: int):
    return "delete todo item with id {id}"

@app.get("/todo")
def read_todo_list():
    return "read todo list"



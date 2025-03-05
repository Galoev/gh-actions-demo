from fastapi import FastAPI

app = FastAPI()

tasks = ['1. Task', '2. Task', '3. Hello world']

@app.get("/")
def read_tasks():
    return {"tasks": tasks}

@app.post("/add")
def add_task(task: str):
    tasks.append(task)
    return {"message": "Task added"}

from fastapi import FastAPI

app = FastAPI()

tasks = []


@app.get("/")
def read_tasks():
    return {"tasks": tasks}

@app.post("/add")
def add_task(task: str):
    tasks.append(task)
    return {"message": task}

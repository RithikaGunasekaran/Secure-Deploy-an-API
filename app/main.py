from fastapi import FastAPI, Depends, HTTPException
from app.auth import create_token, verify_token

app = FastAPI()

fake_tasks = []

@app.get("/")
def read_root():
    return {"message": "API Running"}

@app.post("/login")
def login():
    token = create_token({"user": "admin"})
    return {"access_token": token}

@app.get("/tasks")
def get_tasks(user=Depends(verify_token)):
    return fake_tasks

@app.post("/tasks")
def add_task(task: dict, user=Depends(verify_token)):
    fake_tasks.append(task)
    return {"message": "Task added"}
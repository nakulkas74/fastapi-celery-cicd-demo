# Create hello world FastAPI app
from fastapi import FastAPI
import celery_demo

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "It's working!"}

@app.post("/create_task/")
async def create_task(expire_time: int):
    task_details = celery_demo.run_task(expire_time)
    return task_details

@app.post("/get_task_status/")
async def get_task_status(task_id: str):
    task_details = celery_demo.get_status(str(task_id))
    return task_details
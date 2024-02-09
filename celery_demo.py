from celery_config import celery_app
import utils

import redis
import time
import os
from celery.result import AsyncResult
from dotenv import load_dotenv
load_dotenv('.env')

celery_backend_db = os.environ.get("CELERY_RESULT_BACKEND")

@celery_app.task(name="create_task")
def create_task(stop_time,email_id):
    time.sleep(int(stop_time))
    receiver_email_list = [email_id]
    email_title = 'Competitor asins file is ready'
    email_descp = 'Your competitor asins file is ready go and visit {url} to get access of the file'
    utils.email_link(receiver_email_list, email_title, email_descp)
    return {'stoptime':int(stop_time),'email_id':email_id}

def delete_task_data_from_redis(task_id):
    redis_host, port_db = celery_backend_db.split("://")[1].split(":")
    redis_port, redis_db = port_db.split("/")

    redis_port = int(redis_port)
    redis_db = int(redis_db)
    
    r = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
    r.delete(f"celery-task-meta-{task_id}")
    
def run_task(task_type: int, email_id: str):
    task = create_task.delay(int(task_type),email_id)
    print(task.id)
    return {"task_id": task.id}

def get_status(task_id: str):
    task_result = AsyncResult(task_id,app=celery_app)
    
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    
    # if task_result.result:
    #     delete_task_data_from_redis(task_id)
    #     print('task done')
    
    return result
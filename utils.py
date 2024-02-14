from send_mail import SendMail
import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv('.env')
sender_email = 'nakulchamariya373@gmail.com'
sender_password = 'gnhcjjvsjznxvodv'

# MongoDB configuration
mongo_host = os.environ.get("MONGO_HOST", "127.0.0.1")
mongo_port = int(os.environ.get("MONGO_PORT", 27017))
mongo_db_name = os.environ.get("CELERY_MONGO_DB", "celery_jobs")
taskmeta_collection_name = os.environ.get("CELERY_MONGO_COLLECTION", "celery_taskmeta")

# Connect to MongoDB
client = MongoClient(mongo_host, mongo_port)
db = client[mongo_db_name]
taskmeta_collection = db[taskmeta_collection_name]

def get_celery_task_result(task_id):
    # Query the taskmeta collection based on task_id
    result = taskmeta_collection.find_one({"_id": task_id})

    # Extract the result from the metadata
    if result:
        return result.get("result")
    else:
        return None

def email_link(receiver_email_list, email_title, email_descp):
    new_mail = SendMail(receiver_email_list, email_title, email_descp, sender_email)
    new_mail.send(sender_password)
    
if __name__ == '__main__':
    task_id = 'ac0f38af-695c-4d93-bb1c-9f78eaf84afc'
    results = get_celery_task_result(task_id)
    print(results)
import os
from celery import Celery
from dotenv import load_dotenv
load_dotenv('.env')

celery_app = Celery(__name__)
celery_app.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery_app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")
celery_app.conf.result_expires = os.environ.get("CELERY_RESULT_EXPIRE")
celery_app.conf.include = [
    'celery_demo',
]
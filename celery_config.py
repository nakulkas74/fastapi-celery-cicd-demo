import os
from celery import Celery
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('.env')

# Create Celery instance
celery_app = Celery(__name__)

# Set broker connection retry on startup
celery_app.conf.broker_connection_retry_on_startup = True

# Configure Celery to use the provided broker URL
celery_app.conf.broker_url = os.environ.get("CELERY_BROKER_URL")

# Configure Celery to use MongoDB as the result backend
celery_app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")
celery_app.conf.result_backend_settings = {
    "host": os.environ.get("MONGO_HOST", "127.0.0.1"),
    "port": int(os.environ.get("MONGO_PORT", 27017)),
    "database": os.environ.get("CELERY_MONGO_DB", "celery"),
    "taskmeta_collection": os.environ.get("CELERY_MONGO_COLLECTION", "celery_taskmeta"),
}

# Set result_expires to a large value or None to disable expiration
celery_app.conf.result_expires = os.environ.get("CELERY_RESULT_EXPIRE")

# Additional Celery configuration
celery_app.conf.include = [
    'celery_demo',
]
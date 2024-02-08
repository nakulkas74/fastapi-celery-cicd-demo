#!/bin/bash
if [ "$1" == "celery" ]; then
    exec celery -A celery_config worker --loglevel=info
else
    python -m uvicorn main:app --host 0.0.0.0 --port 8080 --reload
fi
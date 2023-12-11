from celery import Celery


celery = Celery(
    'tasks',
    broker='reddis://localhost',
    include=['app.tasks.tasks']
)
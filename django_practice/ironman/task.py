# myproject/tasks.py
# 任務
from celery import Celery
from celery import shared_task
import time

app = Celery("myproject")


@app.task
def test():
    pass


@shared_task
def add(x, y):
    time.sleep(2)
    return x + y

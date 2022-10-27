# myproject/tasks.py
# 专属于myproject项目的任务
from celery import Celery
app = Celery('myproject')
@ app.task
def test():
    pass

# app/tasks.py, 可以复用的task
from celery import shared_task
import time

@shared_task
def add(x, y):
    time.sleep(2)
    return x + y
import random

from celery import Celery

# no backend
# app = Celery("tasks", broker="pyamqp://guest@localhost")
app = Celery('tasks', backend='rpc://', broker='pyamqp://')

@app.task
def add(x, y):
    if random.random() > 0.5:
        raise ValueError(f"Some error occured")
    return x + y
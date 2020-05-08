import time
from celery import Celery

app = Celery('tasks', broker='amqp://localhost//', backend='db+postgresql://andyphied:Ericphilip5@localhost/task_db')

@app.task
def reverse(string):
    time.sleep(10)
    return string[::-1]
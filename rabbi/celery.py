from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rabbi.settings')

# app = Celery('rabbi')
app = Celery('rabbi', backend='redis://localhost', broker='amqp://localhost//')
# app = Celery(
#     "rabbi",
#     broker='pyamqp://guest:guest@rabbitmq.insertmendoza.com.ar',
#     include=["rabbi.Apps.TaskManager.Tasks"]
# )


app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.schedule_beat = {
    'every-15-secounds': {
        'task': 'results.tasks.send_email',
        'schedule': 15,
        'args': ('kumshiv166@gmail.com',)
    }
}
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
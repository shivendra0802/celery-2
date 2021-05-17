from __future__ import absolute_import, unicode_literals

from celery import shared_task


@shared_task
def add(x, y):
    return x + y 

@shared_task
def send_email(email):
    print(f'A sample message is sent to {email}')

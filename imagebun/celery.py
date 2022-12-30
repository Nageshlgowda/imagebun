# https://www.accordbox.com/blog/how-to-setup-celery-django/
from __future__ import absolute_import
import os
from celery import Celery
from imagebun import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imagebun.settings')

app = Celery("imagebun")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def add(x, y):
    return x / y

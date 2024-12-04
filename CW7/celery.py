import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CW7.settings')

app = Celery('CW7')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
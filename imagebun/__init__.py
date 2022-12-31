from __future__ import absolute_import, unicode_literals

from .celery import app as celery_app
# import below to make task in celery worker otherwise you will see message ignore error.
# from imgbun import tasks


__all__ = ('celery_app',)
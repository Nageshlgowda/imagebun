from imagebun import celery_app
from imgbun.models import *
import time
#
#
# @celery_app.task
# def imagebun_celery(create_entry):
#     # time.sleep(10)
#     created_entry = imgdb.objects.get(id=create_entry.id)
#     return created_entry.to_dict()

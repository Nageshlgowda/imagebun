from imagebun import celery_app
from imagebun.settings import *
import requests
from imgbun.models import imgdb


@celery_app.task
def imagebun_celery(image_data):

    api_key = IMAGEBUN_APIKEY_SET
    payload = {
        'key': api_key,
        'text': image_data.get("text"),
        'color': image_data.get("color"),
        'size': image_data.get("size"),
        'background': image_data.get("background"),
    }
    get_request = requests.get(IMAGEBUN_ENDPOINT, params=payload)

    # db_row = imgdb.objects.get(id=image_data.get("id"))
    # db_row.imagebun_link = get_request.get('direct_link')
    # db_row.status = True
    # db_row.save()

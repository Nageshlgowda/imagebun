from imagebun import celery_app
from imagebun.settings import IMAGEBUN_ENDPOINT
import requests
import os


@celery_app.task
def imagebun_celery(image_data):
    api_key = os.environ.get('IMAGEBUN_APIKEY')
    payload = {
        'key': api_key,
        'text': image_data.get("text"),
        'color': image_data.get("color"),
        'size': image_data.get("size"),
        'background': image_data.get("background"),
    }

    get_request = requests.get(IMAGEBUN_ENDPOINT, params=payload)

    print(payload)

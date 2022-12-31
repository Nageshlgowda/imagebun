from imagebun import celery_app
from imagebun.settings import IMAGEBUN_ENDPOINT



@celery_app.task
def imagebun_celery(image_dat):
    # payload = {'q': 'food'}
    # r = requests.get(IMAGEBUN_ENDPOINT, params=payload)
    print(image_dat)

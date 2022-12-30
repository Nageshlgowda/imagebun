from imagebun import celery_app


@celery_app.task
def imagebun_api(x, y):
    """
    this is a async task to do something

    :param x: explain x
    :param y: explain y
    :return: this is the return explanation
    """
    # data in

    return x - y

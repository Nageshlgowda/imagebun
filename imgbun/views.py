from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from imgbun.models import *
from .tasks import imagebun_celery
import os
def frontpage(request):
    data = "Front page html test ___working"
    return JsonResponse({"data": data})


@csrf_exempt
def image(request):
    image_data = json.loads(request.body.decode())

    create_entry = imgdb.objects.create(
        img_format=image_data.get("format"),
        text=image_data.get("text"),
        color=image_data.get("color"),
        background=image_data.get("background"),
    )
    result_from_celery = imagebun_celery.delay(image_data)
    return JsonResponse(create_entry.to_dict())


def status(request, id):
    post = imgdb.objects.get(id=id)
    if not post.status:
        return JsonResponse({"status": "procesing"})
    else:
        link = {"status": post.imagebun_link}
        return JsonResponse(link)


def delete(request, id):
    post = imgdb.objects.filter(id=id).delete()
    return JsonResponse({"id": id, "status": "deleted"})

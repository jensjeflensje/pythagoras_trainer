from django.shortcuts import render
from django.http import JsonResponse
from . import img_helper
import random
import os


def home(request):
    return render(request, "index.html")


def get_img(request):
    img, data, answer = img_helper.create_triangle()
    rand = str(random.randint(0, 10000))
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    img_path = base_dir + "\\static\\" + rand + ".png"
    img.save(img_path)
    print(answer)
    return JsonResponse({
        "img": "/static/" + rand + ".png",
        "answer": answer,
    })

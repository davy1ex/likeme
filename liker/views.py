from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User


def get_like(request, user_id):    
    return HttpResponse(User.objects.get(id=user_id).likerer.like)


def like(request, user_id):
    u = User.objects.get(id=user_id).likerer
    u.like += 1
    u.save()
    return HttpResponse("True")


def user_page(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, "index.html", {
        "user": user,
    })

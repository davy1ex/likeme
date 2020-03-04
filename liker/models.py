from django.db import models

from django.contrib.auth.models import User


class Likerer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

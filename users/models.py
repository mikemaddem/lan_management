from django.db import models
from django.contrib.auth.models import User


class LANUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='lan-django-user')
    name = models.CharField()

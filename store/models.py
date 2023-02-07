from django.db import models


class SubscriptionOption(models.Model):
    name = models.CharField(max_length=30)
    price = models.Curr
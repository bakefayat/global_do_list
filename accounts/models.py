from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    default_destination_user = models.ForeignKey("self", default=None, on_delete=models.SET_NULL, null=True, verbose_name="مقصد پیش فرض")
    allowed_destinations = models.ManyToManyField("self", default=None, verbose_name="دوستان")

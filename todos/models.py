from django.db import models
from django.contrib.auth import get_user_model as users
import uuid


class Todos(models.Model):
    class Meta:
        verbose_name = 'وظیفه'
        verbose_name_plural = 'وظایف'

    STATUS_CHOICES = (
        (0, "انجام شده"),
        (1, "در دست اقدام"),
    )
    title = models.TextField(max_length=100, verbose_name='عنوان')
    creator = models.ForeignKey(users(), on_delete=models.SET_NULL, related_name="tasks", null=True,
                                blank=True, verbose_name='سازنده')
    destination = models.ForeignKey(users(), on_delete=models.CASCADE, null=True, blank=True, verbose_name='وظیفه کاربر')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=0, verbose_name='وضعیت')
    unique_id = models.UUIDField(default=uuid.uuid4(), editable=False, unique=True)

    def __str__(self):
        return self.title

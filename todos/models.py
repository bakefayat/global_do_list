from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import get_user_model as users
import uuid

from core.models import TimeStampedModel


class Todos(TimeStampedModel):
    class Meta:
        verbose_name = 'وظیفه'
        verbose_name_plural = 'وظایف'

    STATUS_CHOICES = (
        (0, "انجام شده"),
        (1, "در دست اقدام"),
    )
    title = models.TextField(max_length=100, verbose_name='عنوان',
                             validators=[MinLengthValidator(3, "حداقل طول 3 کاراکتر باشد.")])
    creator = models.ForeignKey(users(), on_delete=models.SET_NULL, related_name="tasks", null=True,
                                blank=True, verbose_name='سازنده')
    destination = models.ForeignKey(users(), on_delete=models.CASCADE, null=True, blank=True, verbose_name='وظیفه کاربر')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name='وضعیت')
    unique_id = models.UUIDField(editable=False, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = uuid.uuid4()
        super(Todos, self).save(*args, **kwargs)

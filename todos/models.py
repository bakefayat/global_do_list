from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import get_user_model as users
from django.utils.translation import gettext_lazy as _
import uuid

from core.models import TimeStampedModel


class Todos(TimeStampedModel):
    class Meta:
        verbose_name = _('todo')
        verbose_name_plural = _('todos')

    STATUS_CHOICES = (
        (0, _('completed')),
        (1, _('working on it')),
    )
    title = models.TextField(max_length=100, verbose_name=_('title'),
                             validators=[MinLengthValidator(3, _('minimum length should be 3 characters'))])
    creator = models.ForeignKey(users(), on_delete=models.SET_NULL, related_name="tasks", null=True,
                                blank=True, verbose_name=_('creator'))
    destination = models.ForeignKey(users(), on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('destination'))
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name=_('status'))
    unique_id = models.UUIDField(editable=False, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = uuid.uuid4()
        super(Todos, self).save(*args, **kwargs)

from django.db import models
from django.contrib.auth import get_user_model


class Todos(models.Model):
    class Meta:
        verbose_name = 'وظیفه'
        verbose_name_plural = 'وظایف'

    STATUS_CHOICES = (
        ("co", "انجام شده"),
        ("on", "در دست اقدام"),
        ("un", "اقدام نشده"),
    )
    title = models.TextField(max_length=100, verbose_name='عنوان')
    destination = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None, verbose_name='وظیفه کاربر')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='un', verbose_name='وضعیت')

    def __str__(self):
        return self.title

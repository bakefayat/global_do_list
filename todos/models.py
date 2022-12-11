from django.db import models
from django.contrib.auth import get_user_model as users


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
    creator = models.ForeignKey(users(), on_delete=models.SET_NULL, related_name="tasks", null=True,
                                default=None, verbose_name='سازنده')
    destination = models.ForeignKey(users(), on_delete=models.CASCADE, default=None, verbose_name='وظیفه کاربر')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='un', verbose_name='وضعیت')

    def __str__(self):
        return self.title

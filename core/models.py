from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="تاریخ ساخت")
    modified = models.DateTimeField(auto_now=True, null=True, verbose_name="آخرین بروزرسانی")

    class Meta:
        abstract = True

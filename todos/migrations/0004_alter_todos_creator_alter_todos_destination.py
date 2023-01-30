# Generated by Django 4.1.4 on 2023-01-30 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todos', '0003_todos_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='creator',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='سازنده'),
        ),
        migrations.AlterField(
            model_name='todos',
            name='destination',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='وظیفه کاربر'),
        ),
    ]
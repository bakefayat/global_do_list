# Generated by Django 4.1.4 on 2023-02-02 07:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0008_todos_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='status',
            field=models.IntegerField(choices=[(0, 'انجام شده'), (1, 'در دست اقدام')], default=0, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='todos',
            name='unique_id',
            field=models.UUIDField(default=uuid.UUID('2080fc8b-79db-4606-b637-d635ad10b7df'), editable=False, unique=True),
        ),
    ]

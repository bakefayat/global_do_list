# Generated by Django 4.1.4 on 2022-12-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100, verbose_name='عنوان')),
                ('status', models.CharField(choices=[('co', 'انجام شده'), ('on', 'در دست اقدام'), ('un', 'اقدام نشده')], default='un', max_length=2, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'وظیفه',
                'verbose_name_plural': 'وظایف',
            },
        ),
    ]
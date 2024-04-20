# Generated by Django 5.0.4 on 2024-04-13 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=datetime.datetime(2024, 4, 13, 15, 34, 16, 318455, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=datetime.datetime(2024, 4, 13, 15, 34, 30, 532182, tzinfo=datetime.timezone.utc), max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.URLField(default=datetime.datetime(2024, 4, 13, 15, 34, 37, 817397, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
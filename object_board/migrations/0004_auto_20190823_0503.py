# Generated by Django 2.2.4 on 2019-08-22 20:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('object_board', '0003_obpost_finish'),
    ]

    operations = [
        migrations.AddField(
            model_name='obpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 8, 22, 20, 2, 46, 63137, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obpost',
            name='goal',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

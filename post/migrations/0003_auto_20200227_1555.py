# Generated by Django 2.2.3 on 2020-02-27 15:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200227_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 27, 15, 54, 1, 491153, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=datetime.datetime(2020, 2, 27, 15, 54, 44, 184048, tzinfo=utc), upload_to='media/post/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 27, 15, 55, 8, 572377, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2020, 2, 27, 15, 55, 45, 261688, tzinfo=utc), editable=False, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]

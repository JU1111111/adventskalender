# Generated by Django 4.2.3 on 2023-08-26 17:31

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vidPlatform', '0003_dateentry_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dateentry',
            name='date',
        ),
        migrations.AddField(
            model_name='dateentry',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='end quiz on'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dateentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 26, 17, 31, 33, 138237, tzinfo=datetime.timezone.utc), verbose_name='date published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dateentry',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 26, 17, 31, 48, 829720, tzinfo=datetime.timezone.utc), verbose_name='start quiz on'),
            preserve_default=False,
        ),
    ]

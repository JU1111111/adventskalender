# Generated by Django 4.2.5 on 2023-09-08 19:12

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vidPlatform', '0007_alter_dateentry_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='dateentry',
            name='resolutionVidLink',
            field=models.CharField(default=django.utils.timezone.now, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dateentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 8, 21, 12, 21, 671353), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='dateentry',
            name='videoLink',
            field=models.CharField(max_length=64),
        ),
    ]

# Generated by Django 4.2.5 on 2023-12-04 21:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidPlatform', '0024_alter_dateentry_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 22, 47, 21, 821484), verbose_name='date published'),
        ),
    ]

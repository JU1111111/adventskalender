# Generated by Django 4.2.5 on 2023-09-08 19:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidPlatform', '0010_alter_choice_iscorrect_alter_dateentry_pub_date_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 8, 21, 31, 56, 361985), verbose_name='date published'),
        ),
    ]
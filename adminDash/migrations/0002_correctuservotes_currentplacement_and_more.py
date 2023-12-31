# Generated by Django 4.2.5 on 2023-12-04 21:50

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminDash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='correctuservotes',
            name='currentPlacement',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='correctuservotes',
            name='displayName',
            field=models.CharField(default='yeet', max_length=32),
        ),
        migrations.AddField(
            model_name='correctuservotes',
            name='isStudent',
            field=models.BooleanField(default=False, verbose_name='is a valid student'),
        ),
        migrations.AddField(
            model_name='correctuservotes',
            name='lastRefresh',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='letzes Update'),
        ),
    ]

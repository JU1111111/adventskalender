# Generated by Django 4.2.3 on 2023-08-26 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidPlatform', '0002_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='dateentry',
            name='title',
            field=models.CharField(blank=True, max_length=340, null=True),
        ),
    ]

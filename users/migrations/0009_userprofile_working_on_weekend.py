# Generated by Django 3.0.2 on 2020-02-17 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200213_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='working_on_weekend',
            field=models.BooleanField(default=False),
        ),
    ]
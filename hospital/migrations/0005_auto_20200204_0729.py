# Generated by Django 3.0.2 on 2020-02-04 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specializations', '0001_initial'),
        ('hospital', '0004_auto_20200204_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='specialization',
            field=models.ManyToManyField(blank=True, to='specializations.Specialization'),
        ),
    ]

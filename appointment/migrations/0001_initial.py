# Generated by Django 3.0.2 on 2020-01-31 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.BaseModel')),
                ('time_slot', models.DateField()),
                ('notes', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('app.basemodel',),
        ),
    ]
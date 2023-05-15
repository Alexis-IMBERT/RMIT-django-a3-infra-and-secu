# Generated by Django 4.2.1 on 2023-05-15 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiplomaNumber',
            fields=[
                ('diploma_number', models.IntegerField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('programe_name', models.CharField(max_length=500)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-19 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_rename_username_diplomanumber_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diplomanumber',
            name='diploma_number',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
        ),
    ]

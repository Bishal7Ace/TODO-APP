# Generated by Django 5.2 on 2025-04-12 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]

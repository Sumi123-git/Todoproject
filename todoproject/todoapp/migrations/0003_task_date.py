# Generated by Django 3.2.11 on 2022-01-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20220118_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-02-22'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0.2 on 2018-03-07 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curhats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
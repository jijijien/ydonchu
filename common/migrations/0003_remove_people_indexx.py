# Generated by Django 3.2.7 on 2021-11-06 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20211106_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='indexx',
        ),
    ]

# Generated by Django 3.2.7 on 2021-11-07 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0004_auto_20211107_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='who',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.7 on 2021-11-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_remove_people_indexx'),
    ]

    operations = [
        migrations.CreateModel(
            name='What_food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_many', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('who', models.TextField(default='')),
                ('date', models.DateField()),
            ],
        ),
    ]

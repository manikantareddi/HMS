# Generated by Django 2.1.3 on 2018-11-27 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_bookinginformation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinginformation',
            name='requirements',
        ),
        migrations.AddField(
            model_name='bookinginformation',
            name='no_of_rooms',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='bookinginformation',
            name='room',
            field=models.CharField(default='Not Selected', max_length=100),
        ),
    ]

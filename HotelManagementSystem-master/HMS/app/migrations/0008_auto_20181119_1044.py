# Generated by Django 2.1.3 on 2018-11-19 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20181119_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roombooking',
            old_name='check_in',
            new_name='checkin',
        ),
        migrations.RenameField(
            model_name='roombooking',
            old_name='check_out',
            new_name='checkout',
        ),
    ]
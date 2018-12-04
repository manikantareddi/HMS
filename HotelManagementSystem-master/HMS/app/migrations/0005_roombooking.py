# Generated by Django 2.1.3 on 2018-11-17 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_hotelbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.CharField(max_length=50)),
                ('check_out', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('hotel_name', models.CharField(max_length=10)),
                ('room', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'roombooking',
            },
        ),
    ]

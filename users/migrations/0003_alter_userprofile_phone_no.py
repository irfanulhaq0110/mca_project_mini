# Generated by Django 4.2 on 2023-04-11 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_driveprofile_driverprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_no',
            field=models.IntegerField(max_length=10),
        ),
    ]

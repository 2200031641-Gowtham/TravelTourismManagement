# Generated by Django 5.0 on 2024-01-03 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_usermodel_name_usermodel_username_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='usermodel',
            table='newUsers',
        ),
    ]

# Generated by Django 5.0 on 2024-01-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0007_delete_usermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='userModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'ttm_users',
            },
        ),
    ]

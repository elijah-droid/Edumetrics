# Generated by Django 4.1.7 on 2023-04-08 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolAdministrators', '0005_schooladministrator_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schooladministrator',
            name='permissions',
        ),
    ]

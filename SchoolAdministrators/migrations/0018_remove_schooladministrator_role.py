# Generated by Django 3.2 on 2023-05-08 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolAdministrators', '0017_adminship_date_authorised'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schooladministrator',
            name='role',
        ),
    ]

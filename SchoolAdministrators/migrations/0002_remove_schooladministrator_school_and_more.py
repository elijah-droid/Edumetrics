# Generated by Django 4.1.7 on 2023-02-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schools', '0001_initial'),
        ('SchoolAdministrators', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schooladministrator',
            name='school',
        ),
        migrations.AddField(
            model_name='schooladministrator',
            name='schools',
            field=models.ManyToManyField(to='Schools.school'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-14 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Schools', '0024_school_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='Parents',
        ),
    ]

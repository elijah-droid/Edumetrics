# Generated by Django 4.1.7 on 2023-04-10 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolAdministrators', '0015_adminship_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminship',
            name='unauthorized_attempts',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]

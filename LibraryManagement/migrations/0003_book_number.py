# Generated by Django 4.1.7 on 2023-04-13 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManagement', '0002_alter_lendout_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Number',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]

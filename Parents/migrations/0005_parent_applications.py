# Generated by Django 4.1.7 on 2023-04-21 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applications', '0002_alter_application_school'),
        ('Parents', '0004_parent_fees_payments'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='applications',
            field=models.ManyToManyField(blank=True, to='Applications.application'),
        ),
    ]

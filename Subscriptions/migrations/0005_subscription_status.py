# Generated by Django 3.2 on 2023-06-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subscriptions', '0004_auto_20230601_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='Status',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

# Generated by Django 3.2 on 2023-06-01 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subscriptions', '0003_alter_subscription_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='Mobile_Number',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='Method',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

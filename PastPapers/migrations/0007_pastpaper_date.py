# Generated by Django 4.1.7 on 2023-04-23 13:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PastPapers', '0006_alter_pastpaper_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastpaper',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

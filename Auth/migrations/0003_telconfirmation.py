# Generated by Django 3.2 on 2023-06-16 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_emailconfirmation'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelConfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tel', models.PositiveIntegerField()),
                ('Code', models.CharField(max_length=100)),
            ],
        ),
    ]

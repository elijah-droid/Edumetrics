# Generated by Django 4.1.7 on 2023-03-30 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeesManagement', '0001_initial'),
        ('Schools', '0013_school_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='Dues',
            field=models.ManyToManyField(blank=True, to='FeesManagement.paymentdue'),
        ),
    ]

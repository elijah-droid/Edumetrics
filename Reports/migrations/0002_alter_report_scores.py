# Generated by Django 4.1.7 on 2023-03-04 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='Scores',
            field=models.ManyToManyField(blank=True, to='Reports.score'),
        ),
    ]

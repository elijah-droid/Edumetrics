# Generated by Django 4.1.7 on 2023-04-25 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Levels', '0001_initial'),
        ('Schools', '0030_school_applications'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='Levels',
            field=models.ManyToManyField(blank=True, to='Levels.level'),
        ),
    ]

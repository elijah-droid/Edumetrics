# Generated by Django 4.1.7 on 2023-04-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lessons', '0002_alter_lesson_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='From',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='To',
            field=models.TimeField(null=True),
        ),
    ]

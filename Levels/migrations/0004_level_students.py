# Generated by Django 4.1.7 on 2023-04-30 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0016_student_education_history'),
        ('Levels', '0003_level_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='Students',
            field=models.ManyToManyField(to='Students.student'),
        ),
    ]

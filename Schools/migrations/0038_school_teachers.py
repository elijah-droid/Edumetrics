# Generated by Django 3.2 on 2023-05-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0014_teacher_teachinghistory'),
        ('Schools', '0037_remove_school_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='Teachers',
            field=models.ManyToManyField(through='Teachers.WorkProfile', to='Teachers.Teacher'),
        ),
    ]

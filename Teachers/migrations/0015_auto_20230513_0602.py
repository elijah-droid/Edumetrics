# Generated by Django 3.2 on 2023-05-13 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0014_teacher_teachinghistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='current_class',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='current_stream',
        ),
    ]

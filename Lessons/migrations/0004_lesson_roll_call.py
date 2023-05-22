# Generated by Django 3.2 on 2023-05-21 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0008_rollcall'),
        ('Lessons', '0003_alter_lesson_from_alter_lesson_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='Roll_Call',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Attendance.rollcall'),
        ),
    ]

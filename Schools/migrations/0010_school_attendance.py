# Generated by Django 4.1.7 on 2023-03-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0007_alter_attendance_school'),
        ('Schools', '0009_school_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='attendance',
            field=models.ManyToManyField(blank=True, to='Attendance.attendance'),
        ),
    ]

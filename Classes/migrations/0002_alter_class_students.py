# Generated by Django 4.1.7 on 2023-03-08 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0006_remove_student_sujects_student_subjects'),
        ('Classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='Students',
            field=models.ManyToManyField(blank=True, to='Students.student'),
        ),
    ]

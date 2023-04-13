# Generated by Django 4.1.7 on 2023-04-13 13:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Classes', '0007_class_lessons_alter_class_class_teacher_and_more'),
        ('Schools', '0023_alter_school_current_term'),
        ('Students', '0012_student_active_enrollment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('For_Classes', models.ManyToManyField(to='Classes.class')),
            ],
        ),
        migrations.CreateModel(
            name='LendOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(default=datetime.datetime(2023, 4, 13, 13, 2, 4, 231042))),
                ('Returned', models.BooleanField(default=False)),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryManagement.book')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.student')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='Lend_Outs',
            field=models.ManyToManyField(blank=True, to='LibraryManagement.lendout'),
        ),
        migrations.AddField(
            model_name='book',
            name='School',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schools.school'),
        ),
    ]

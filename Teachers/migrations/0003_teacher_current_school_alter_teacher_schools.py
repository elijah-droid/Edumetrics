# Generated by Django 4.1.7 on 2023-02-28 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitments', '0002_classrecruitment_school'),
        ('Schools', '0001_initial'),
        ('Teachers', '0002_teacher_schools'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='current_school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Schools.school'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='Schools',
            field=models.ManyToManyField(related_name='work_profile', through='Recruitments.ClassRecruitment', to='Schools.school'),
        ),
    ]

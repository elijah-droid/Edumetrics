# Generated by Django 4.1.7 on 2023-03-19 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0008_remove_teacher_email'),
        ('Subjects', '0003_subject_head_of_department_subject_students_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='Head_Of_Department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='HOD', to='Teachers.teacher'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(choices=[('Mathematics', 'Mathematics'), ('English', 'English'), ('Science', 'Science'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Computer Studies', 'Computer Studies'), ('Social Studies', 'Social Studies'), ('Geography', 'Geography'), ('Christian Religious Education', 'Christian Religious Education'), ('Islamic Religious Education', 'Islamic Religious Education')], max_length=100),
        ),
    ]

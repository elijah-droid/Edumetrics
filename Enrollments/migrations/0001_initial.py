# Generated by Django 4.1.7 on 2023-04-06 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Schools', '0016_school_terms'),
        ('Students', '0010_student_parents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField()),
                ('School', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schools.school')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.student')),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-05 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0001_initial'),
        ('Students', '0002_student_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Classes.class'),
        ),
    ]

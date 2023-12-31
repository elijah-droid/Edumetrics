# Generated by Django 4.1.7 on 2023-02-28 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0001_initial'),
        ('Streams', '0001_initial'),
        ('Teachers', '0003_teacher_current_school_alter_teacher_schools'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='current_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Classes.class'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='current_stream',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Streams.stream'),
        ),
    ]

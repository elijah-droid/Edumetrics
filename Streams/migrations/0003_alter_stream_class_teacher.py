# Generated by Django 4.1.7 on 2023-05-02 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0014_teacher_teachinghistory'),
        ('Streams', '0002_stream_class_stream_class_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='Class_Teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Teachers.teacher'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-08 17:20

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0006_remove_student_sujects_student_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='Students/Photos'),
        ),
    ]

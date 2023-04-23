# Generated by Django 4.1.7 on 2023-04-23 11:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PastPapers', '0002_alter_pastpaper_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastpaper',
            name='Answers_Pdf',
            field=models.FileField(blank=True, null=True, upload_to='PastPapers/Answers', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AlterField(
            model_name='pastpaper',
            name='Questions_Pdf',
            field=models.FileField(upload_to='PastPapers/Papers', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]

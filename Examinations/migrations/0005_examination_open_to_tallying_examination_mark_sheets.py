# Generated by Django 4.1.7 on 2023-04-26 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarkSheets', '0002_marksheet_subject_alter_marksheet_tallies'),
        ('Examinations', '0004_examination_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='examination',
            name='Open_To_Tallying',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='examination',
            name='mark_sheets',
            field=models.ManyToManyField(to='MarkSheets.marksheet'),
        ),
    ]

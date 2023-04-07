# Generated by Django 4.1.7 on 2023-04-07 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0006_report_aggregate'),
        ('Schools', '0017_school_enrollments'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='Reports',
            field=models.ManyToManyField(blank=True, related_name='school_reports', to='Reports.report'),
        ),
    ]

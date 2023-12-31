# Generated by Django 4.1.7 on 2023-03-04 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Examinations', '0004_examination_classes'),
        ('Events', '0002_event_school'),
        ('Schools', '0003_school_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='Events',
            field=models.ManyToManyField(blank=True, related_name='school_events', to='Events.event'),
        ),
        migrations.AddField(
            model_name='school',
            name='Examinations',
            field=models.ManyToManyField(blank=True, to='Examinations.examination'),
        ),
    ]

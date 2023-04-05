# Generated by Django 4.1.7 on 2023-04-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Terms', '0001_initial'),
        ('Schools', '0015_school_current_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='Terms',
            field=models.ManyToManyField(blank=True, related_name='school_terms', to='Terms.term'),
        ),
    ]

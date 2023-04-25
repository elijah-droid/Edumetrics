# Generated by Django 4.1.7 on 2023-04-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requirements', '0002_requirement_delete_requirements'),
        ('Programmes', '0004_remove_programme_requirements'),
    ]

    operations = [
        migrations.AddField(
            model_name='programme',
            name='Requirements',
            field=models.ManyToManyField(blank=True, to='Requirements.requirement'),
        ),
    ]

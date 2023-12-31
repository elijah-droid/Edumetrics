# Generated by Django 4.1.7 on 2023-02-26 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Schools', '0001_initial'),
        ('SchoolAdministrators', '0002_remove_schooladministrator_school_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schooladministrator',
            name='current_school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_school', to='Schools.school'),
        ),
    ]

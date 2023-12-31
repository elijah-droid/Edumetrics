# Generated by Django 4.1.7 on 2023-04-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schools', '0020_school_parents_alter_school_administrators'),
        ('SchoolAdministrators', '0011_remove_schooladministrator_schools'),
    ]

    operations = [
        migrations.AddField(
            model_name='schooladministrator',
            name='schools',
            field=models.ManyToManyField(through='SchoolAdministrators.Adminship', to='Schools.school'),
        ),
    ]

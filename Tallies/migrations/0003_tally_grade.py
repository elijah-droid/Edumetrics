# Generated by Django 4.1.7 on 2023-04-20 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Grading', '0003_alter_grade_name'),
        ('Tallies', '0002_remove_tally_from_remove_tally_to_remove_tally_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tally',
            name='Grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Grading.grade'),
        ),
    ]

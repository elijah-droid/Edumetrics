# Generated by Django 4.1.7 on 2023-04-09 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0012_student_active_enrollment'),
        ('FeesManagement', '0002_paymentdue_term'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='Students',
        ),
        migrations.AddField(
            model_name='payment',
            name='Student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Students.student'),
        ),
    ]

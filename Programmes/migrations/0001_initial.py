# Generated by Django 4.1.7 on 2023-04-14 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Students', '0012_student_active_enrollment'),
        ('FeesManagement', '0006_paymentdue_compulsory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(choices=[('Boarding', 'Boarding'), ('Day School', 'Day School')], max_length=100)),
                ('Fees', models.ManyToManyField(blank=True, to='FeesManagement.paymentdue')),
                ('Students', models.ManyToManyField(blank=True, to='Students.student')),
            ],
        ),
    ]

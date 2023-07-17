# Generated by Django 3.2 on 2023-07-15 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeesManagement', '0007_payment_paid_via'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('MTNUG', 'MTNUG'), ('AIRTELUG', 'AIRTELUG'), ('Other', 'Other')], max_length=20),
        ),
    ]

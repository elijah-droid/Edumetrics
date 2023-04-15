# Generated by Django 4.1.7 on 2023-04-14 09:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Terms', '0001_initial'),
        ('FeesManagement', '0004_paymentdue_payments'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='paymentdue',
            name='Term',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Terms.term'),
        ),
    ]

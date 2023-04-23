# Generated by Django 4.1.7 on 2023-04-23 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Teachers', '0012_workprofile_lessons'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=100)),
                ('Questions_Pdf', models.FileField(upload_to='PastPapers/Papers')),
                ('Answers_Pdf', models.FileField(upload_to='PastPapers/Answers')),
                ('Description', models.TextField(max_length=1000)),
                ('Price', models.PositiveIntegerField()),
                ('Downloads', models.PositiveIntegerField()),
                ('Teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teachers.teacher')),
            ],
        ),
    ]

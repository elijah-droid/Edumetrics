# Generated by Django 4.1.7 on 2023-03-29 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0009_alter_student_photo'),
        ('Parents', '0002_parent_subscribed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='children',
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Relationship', models.CharField(choices=[('Mother', 'Mother'), ('Father', 'Father'), ('Aunt', 'Aunt'), ('Uncle', 'Uncle'), ('GrandMother', 'GrandMother'), ('GrandFather', 'GrandFather')], max_length=100)),
                ('Child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.student')),
                ('Parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Parents.parent')),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='relationships',
            field=models.ManyToManyField(blank=True, to='Parents.relationship'),
        ),
    ]

# Generated by Django 4.2.15 on 2024-08-30 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_batch_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batch',
            old_name='Department',
            new_name='department',
        ),
        migrations.RemoveField(
            model_name='student',
            name='bach_time',
        ),
        migrations.RemoveField(
            model_name='student',
            name='joined_date',
        ),
    ]

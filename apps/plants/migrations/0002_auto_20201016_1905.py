# Generated by Django 3.1.2 on 2020-10-16 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantevent',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='plantevent',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='userplant',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='userplant',
            name='updated_by',
        ),
    ]

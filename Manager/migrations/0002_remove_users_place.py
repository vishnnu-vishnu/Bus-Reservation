# Generated by Django 5.0.2 on 2024-02-20 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='place',
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0014_remove_users_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

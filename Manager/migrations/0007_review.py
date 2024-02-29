# Generated by Django 5.0.1 on 2024-02-28 17:18

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0006_buses_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.CharField(max_length=300)),
                ('bus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Manager.buses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.users')),
            ],
        ),
    ]
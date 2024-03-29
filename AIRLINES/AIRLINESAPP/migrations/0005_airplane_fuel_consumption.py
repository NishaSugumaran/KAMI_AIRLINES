# Generated by Django 5.0.1 on 2024-01-27 08:32

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIRLINESAPP', '0004_remove_airplane_fuel_consumption'),
    ]

    operations = [
        migrations.AddField(
            model_name='airplane',
            name='fuel_consumption',
            field=models.GeneratedField(db_persist=True, expression=django.db.models.expressions.CombinedExpression(models.F('airplane_id'), '*', models.Value(200)), output_field=models.IntegerField()),
        ),
    ]

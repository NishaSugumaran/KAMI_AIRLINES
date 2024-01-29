# Generated by Django 5.0.1 on 2024-01-27 08:49

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIRLINESAPP', '0006_remove_airplane_fuel_capacity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='airplane',
            name='fuel_capacity',
            field=models.GeneratedField(db_persist=True, expression=django.db.models.expressions.CombinedExpression(models.F('airplane_id'), '*', models.Value(200)), output_field=models.IntegerField()),
        ),
    ]

# Generated by Django 5.1 on 2025-01-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bike_EF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Engine_cc', models.IntegerField()),
                ('kg_per_km', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='bus_EF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_bus', models.CharField(max_length=200)),
                ('kg_per_km', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='car_EF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kg_per_km', models.FloatField()),
                ('Engine_cc', models.IntegerField()),
                ('type_of_car', models.CharField(max_length=200)),
            ],
        ),
    ]

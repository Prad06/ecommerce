# Generated by Django 5.1.3 on 2024-11-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geolocation_zip_code_prefix', models.IntegerField()),
                ('geolocation_lat', models.FloatField(unique=True)),
                ('geolocation_lng', models.FloatField(unique=True)),
                ('geolocation_city', models.CharField(max_length=200)),
                ('geolocation_state', models.CharField(max_length=200)),
            ],
        ),
    ]

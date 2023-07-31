# Generated by Django 4.1.4 on 2023-07-31 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('satTrack', '0005_remove_satellite_manufacturer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='satellite',
            name='apogee',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='description',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='inclination',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='last_tle_update',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='launch_date',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='launch_site',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='name',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='orbit',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='orbital_period',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='perigee',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='satellite_type',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='sensors',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='status',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='swath',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='tle',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='negative_tilting',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='positive_tilting',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='resolution_type',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='resolution_value',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='swath',
        ),
    ]

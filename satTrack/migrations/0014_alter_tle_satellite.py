# Generated by Django 4.1.4 on 2023-08-03 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('satTrack', '0013_tle_date_added_tle_satellite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tle',
            name='satellite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='satTrack.satellite'),
        ),
    ]

# Generated by Django 4.1 on 2022-10-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvaapp', '0013_fine_location_fine_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicledetails',
            name='RCSTATUS',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
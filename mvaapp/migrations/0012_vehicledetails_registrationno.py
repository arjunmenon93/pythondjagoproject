# Generated by Django 4.1 on 2022-10-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvaapp', '0011_vehicledetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicledetails',
            name='REGISTRATIONNO',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
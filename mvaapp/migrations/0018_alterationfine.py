# Generated by Django 4.1 on 2022-10-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvaapp', '0017_vehicledetails_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='alterationfine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REGISTRATIONNO', models.CharField(max_length=100)),
                ('fines', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 4.1 on 2022-09-18 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='drivinglicence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licenceid', models.TextField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('validfrom', models.CharField(max_length=100)),
                ('validto', models.CharField(max_length=100)),
                ('Dateofbirth', models.CharField(max_length=100)),
                ('Bloodgroup', models.TextField(max_length=100)),
                ('vehicleclass', models.CharField(max_length=100)),
            ],
        ),
    ]

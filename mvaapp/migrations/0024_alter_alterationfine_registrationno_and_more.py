# Generated by Django 4.1 on 2023-06-11 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvaapp', '0023_alter_drivinglicence_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alterationfine',
            name='REGISTRATIONNO',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='alterationfine',
            name='date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='alterationfine',
            name='fines',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='alterationfine',
            name='location',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='alterationfine',
            name='status',
            field=models.CharField(max_length=10),
        ),
    ]

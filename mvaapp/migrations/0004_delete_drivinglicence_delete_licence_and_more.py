# Generated by Django 4.1 on 2022-09-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvaapp', '0003_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='drivinglicence',
        ),
        migrations.DeleteModel(
            name='licence',
        ),
        migrations.AlterField(
            model_name='person',
            name='Phonenumber',
            field=models.CharField(max_length=10),
        ),
    ]

# Generated by Django 4.1 on 2023-06-11 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvaapp', '0021_alter_alterationfine_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='phone',
            name='rate',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='phone',
            name='spec',
            field=models.CharField(max_length=10),
        ),
    ]

# Generated by Django 4.1 on 2022-10-08 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvaapp', '0018_alterationfine'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivinglicence',
            name='img',
            field=models.ImageField(default='default', upload_to='images'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0.6 on 2018-07-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Localizr', '0012_auto_20180523_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localizedstring',
            name='value',
            field=models.TextField(),
        ),
    ]

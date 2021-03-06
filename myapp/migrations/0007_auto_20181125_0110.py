# Generated by Django 2.1.2 on 2018-11-25 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20181121_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=42.3149, max_digits=9),
        ),
        migrations.AddField(
            model_name='patients',
            name='lon',
            field=models.DecimalField(decimal_places=6, default=-83.0364, max_digits=9),
        ),
    ]

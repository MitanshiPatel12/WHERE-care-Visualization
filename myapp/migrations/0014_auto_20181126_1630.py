# Generated by Django 2.0.9 on 2018-11-26 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_locationtrack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='emergancy_contact_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='patients',
            name='emergancy_contact_no',
            field=models.IntegerField(blank=True),
        ),
    ]

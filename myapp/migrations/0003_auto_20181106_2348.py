# Generated by Django 2.1.2 on 2018-11-06 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_patients_bod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients',
            old_name='Id',
            new_name='id',
        ),
    ]
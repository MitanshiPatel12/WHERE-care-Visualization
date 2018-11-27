# Generated by Django 2.1.2 on 2018-11-21 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20181106_2348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patients',
            options={'verbose_name_plural': 'Patients'},
        ),
        migrations.AddField(
            model_name='patients',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='patients',
            name='contact',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patients',
            name='disease_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='patients',
            name='docor_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='patients',
            name='emergancy_contact_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='patients',
            name='emergancy_contact_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patients',
            name='medicine_detail',
            field=models.CharField(default='', max_length=200),
        ),
    ]
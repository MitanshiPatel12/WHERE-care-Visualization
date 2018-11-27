from django.db import models
from django.contrib.auth.models import User
from django_google_maps import fields as map_fields

# Create your models here.


class Patients(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(choices=GENDER, max_length=20, default='Male')
    photo = models.ImageField(default='',verbose_name='Photo',
        blank=True,)
    address = map_fields.AddressField(max_length=200,blank=True)
    geolocation = map_fields.GeoLocationField(max_length=100,blank=True)
    contact = models.IntegerField(blank=True)
    docor_name = models.CharField(max_length=100,blank=True)
    disease_name = models.CharField(max_length=200,blank=True)
    medicine_detail = models.CharField(max_length=200,blank=True)
    emergency_contact_name = models.CharField(max_length=200,blank=True)
    emergency_contact_no = models.IntegerField(blank=True)

    dob = models.DateField(default='2018-11-11')

    def __str__(self):
        return self.firstName

    class Meta:
        verbose_name_plural = "Patients"


class LocationTrack(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    address = map_fields.AddressField(max_length=200, blank=True)
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True)
    date = models.DateField(blank=True)
    time = models.TimeField(blank=True)







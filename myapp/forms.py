from django import forms
from .models import Patients
from django.forms.widgets import DateInput
from django_range_slider.fields import RangeSliderField


class PatientForm(forms.ModelForm):
    firstName = forms.CharField(max_length=30,required=False)
    lastName = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, required=False)
    address = forms.CharField(required=False)
    contact = forms.IntegerField(required=False)
    docor_name = forms.CharField(required=False)
    disease_name = forms.CharField(required=False)
    medicine_detail = forms.CharField(required=False)
    emergancy_contact_name = forms.CharField(required=False)
    emergancy_contact_no = forms.IntegerField(required=False)
    photo = forms.ImageField(required=False)
    #dob = forms.DateField(required=True)

    class Meta:
        model = Patients

        fields = ['firstName','lastName','email','photo','dob','address','contact','docor_name','disease_name','medicine_detail','emergency_contact_name','emergency_contact_no']
        widgets = {
                'dob': DateInput(attrs={'type': 'date'})
            }




from django.shortcuts import render,get_object_or_404,redirect
from .models import Patients,LocationTrack
from .forms import PatientForm
import json
from django.utils.html import escapejs,mark_safe
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.


def get_search_data(patients):
    map_patients = [{
        'firstName': patient.firstName,
        'lastName': patient.lastName,
        'email': patient.email,
        'gender': patient.gender,
        'address_detail': patient.address,
        'geolocation': str(patient.geolocation),
        'contact': patient.contact,
        'docor_name': patient.docor_name,
        'disease_name': patient.disease_name,
        'medicine_detail': patient.medicine_detail,
        'emergancy_contact_name': patient.emergency_contact_name,
        'medicine_detail': patient.medicine_detail,
        'emergancy_contact_no': (patient.emergency_contact_no),
        'photo': str(patient.photo)
    } for patient in patients]
    return map_patients


def get_search_track_data(locationTracks):
    locationTracks_map = [{
        'address_detail': locationTrack.address,
        'geolocation': str(locationTrack.geolocation),
        'time': str(locationTrack.time),
    } for locationTrack in locationTracks]
    return locationTracks_map


def map_data(request):
    patients = Patients.objects.all()
    map_patients = get_search_data(patients)
    return render(request, 'map_data.html', {'patients': mark_safe(escapejs(json.dumps(map_patients)))})


def track_data(request):
    locationTracks = LocationTrack.objects.all()
    patients = Patients.objects.all()
    locationTracks_map = get_search_track_data(locationTracks)
    return render(request, 'track_data.html', {'locationTracks_map': mark_safe(escapejs(json.dumps(locationTracks_map))),'patients':patients})


def search(request):
    template = 'map_data.html'
    query = request.GET.get('q')
    patients = Patients.objects.filter(Q(firstName__icontains=query) | Q(lastName__icontains=query))
    map_patients = get_search_data(patients)
    return render(request,template,{'patients': mark_safe(escapejs(json.dumps(map_patients)))})


def search_date(request):
    query = request.GET.get('date')
    locationTracks = LocationTrack.objects.filter(Q(date__exact=query))
    locationTracks_map = get_search_track_data(locationTracks)
    return JsonResponse(locationTracks_map,safe=False)


def search_time(request):
    query = request.GET.get('time_start')
    query1 = request.GET.get('time_end')
    query2 = request.GET.get('date')
    locationTracks = LocationTrack.objects.filter(Q(time__hour__gte=query) & Q(time__hour__lte=query1) & Q(date__exact=query2))
    locationTracks_map = get_search_track_data(locationTracks)
    return JsonResponse(locationTracks_map,safe=False)


def search_dieases(request):
    template = 'map_data.html'
    query = request.GET.get('qd')
    patients = Patients.objects.filter(Q(disease_name__icontains=query))
    map_patients = get_search_data(patients)
    return render(request,template,{'patients': mark_safe(escapejs(json.dumps(map_patients)))})


def about_us(request):
    return render(request,'about_us.html')


def list_patient(request):
    patients = Patients.objects.all()
    return render(request, 'list_patient.html', { 'patients': patients})


def add_patient(request):
    form = PatientForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('list_patient')
    return render(request, 'add_patient.html', {'form':form})


def edit_patient(request, pk):
    patients= get_object_or_404(Patients, pk=pk)
    form = PatientForm(request.POST or None, instance=patients)
    if form.is_valid():
        form.save()
        return redirect('list_patient')
    return render(request, 'edit_patient.html', {'form':form})


def delete_patient(request, pk):
    patient= get_object_or_404(Patients, pk=pk)
    if request.method=='POST':
        patient.delete()
        return redirect('list_patient')
    return render(request, 'patient_confirm_delete.html', {'object':patient})

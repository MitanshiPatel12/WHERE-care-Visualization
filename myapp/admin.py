from django.contrib import admin

# Register your models here.
from .models import Patients,LocationTrack
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from django.utils.html import mark_safe


class PatientsAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'email', 'photo', 'dob', 'address', 'contact', 'docor_name', 'disease_name',
              'medicine_detail', 'emergency_contact_name', 'emergency_contact_no']

    readonly_fields = ['patient_image']

    formfield_overrides = {
        map_fields.AddressField: {
            'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }

    def patient_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.photo.url,
            width='400px',
            height='400px',
        )
        )


class locationTrackAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'address', 'date', 'time']

    formfield_overrides = {
        map_fields.AddressField: {
            'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }


admin.site.register(Patients,PatientsAdmin)
admin.site.register(LocationTrack,locationTrackAdmin)

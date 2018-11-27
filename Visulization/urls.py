"""Visulization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.map_data,name="map_data"),
    path('track_data/',views.track_data,name="track_data"),

    path('add_patient/', views.add_patient, name='add_patient'),
    path('edit_patient/<int:pk>', views.edit_patient, name='edit_patient'),
    path('delete_patient/<int:pk>', views.delete_patient, name='delete_patient'),
    path('list_patient/', views.list_patient, name='list_patient'),

    path('about_us/', views.about_us, name='about_us'),
    path('search/', views.search, name='search'),
    path('search_dieases/', views.search_dieases, name='search_dieases'),
    path('search_date/', views.search_date, name='search_date'),
    path('search_time/', views.search_time, name='search_time'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

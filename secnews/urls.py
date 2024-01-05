from django.urls import path
from . import views

app_name ="secnew"

urlpatterns = [

    path('',views.main,name ="main"),
    path('csvdownload_incident/',views.csvdownload_incident,name='csvdownload_incident'),
    path('csvdownload_defense/',views.csvdownload_defense,name='csvdownload_defense'),
    path('csvdownload_other/',views.csvdownload_other,name='csvdownload_other'),
    path('xlsxdownload_incident/',views.xlsxdownload_incident,name='xlsxdownload_incident'),
    path('xlsxdownload_defense/',views.xlsxdownload_defense,name='xlsxdownload_defense'),
    path('xlsxdownload_other/',views.xlsxdownload_other,name='xlsxdownload_other'),
    path('csvdownload_overseas/',views.csvdownload_overseas,name='csvdownload_overseas'),
    path('xlsxdownload_overseas/',views.xlsxdownload_overseas,name='xlsxdownload_overseas'),
]

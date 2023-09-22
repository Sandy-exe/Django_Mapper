from django.shortcuts import render
import requests
import folium
from django.http import JsonResponse
from .models import EWaste_facility

# Create your views here.
def Home(request):
    return render(request,'home.html')
def Leaderboard(request):
    return render(request,'leaderboard.html')
def Map(request):
    stations = EWaste_facility.objects.all()
    context = {}
    m = folium.Map(location=[13.0827,80.2707], zoom_start=10)

    for stattion in stations:
        folium.Marker([stattion.latitude, stattion.longitude],popup=stattion.EWaste_facility_name).add_to(m)
    
    context = {'map': m._repr_html_()}
    return render(request, 'map.html', context)
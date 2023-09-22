from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('map/',views.Map,name='map'),
    path('leaderboard/',views.Leaderboard,name='leaderboard'),
]



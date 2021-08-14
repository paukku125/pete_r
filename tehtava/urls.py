from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('solar/', views.solar, name="solar"),
    path('antiqua/', views.antiqua, name="antiqua"),
]
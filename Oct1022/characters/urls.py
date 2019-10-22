from django.urls import path
from . import views

app_name = "characters"

urlpatterns = [
    path('', views.index, name="index"), 
    path('big/create/', views.big_create, name="big_create"),
]
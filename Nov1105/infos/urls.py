from django.urls import path
from . import views

app_name = "infos"

urlpatterns = [
    path('', views.index, name="index"),
    path('one/', views.one_list, name="one_list"),
    path('two/', views.two_list, name="two_list"),
]

from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:id>/', views.detail, name="detail"),
    path('<int:id>/update/', views.update, name="update"),
    path('<int:id>/delete/', views.delete, name="delete"),
    path('<int:id>/create/', views.flavor_create, name="flavor_create"),
    path('<int:coffee_id>/delete/<int:flavor_id>/', views.flavor_delete, name="flavor_delete"),
]

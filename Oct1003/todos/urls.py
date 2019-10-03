# urls.py 생성
from django.urls import path # project의 urls.py에서 복사
from . import views # 추가

urlpatterns = [
    # Read
    path('', views.index),
    # Create
    path('new/', views.new),
    path('create/', views.create),
    # Delete
    path('<int:id>/delete/', views.delete),
    # Update
    path('<int:id>/edit/', views.edit),
    path('<int:id>/update/', views.update),
]
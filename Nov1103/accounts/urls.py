from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('users/', views.user_list, name="user_list"),
    path('<int:user_id>/', views.user_page, name="user_page"),
    path('<int:user_id>/follow/', views.follow, name="follow"),
    path('<int:user_id>/delete/', views.delete, name="delete"),
    path('<int:user_id>/update/', views.update, name="update"),
    path('<int:user_id>/password/', views.password, name="password"),
]

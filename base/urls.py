from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logoutUser, name="logout"),
    path('delete/<str:pk>/', views.delete_profile, name="delete_profile")
]

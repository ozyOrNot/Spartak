from django.urls import path
from . import views

# Импорты для отображения профлильных фото на локальном сервере
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home_page, name="home"),
    path('compare/', views.compare_page, name="compare_page"),

    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logoutUser, name="logout"),
    path('delete/<str:pk>/', views.delete_profile, name="delete_profile"),

    path('sportman-profile/<str:pk>/', views.sportmanProfile, name="sportman-profile"),
    path('edit-profile/<str:pk>/', views.sportmanProfile, name="edit-profile"),
    path('sportman-profile/anthropometry/<str:pk>', views.sportmanAnthropometry, name="sportman-anthropometry"),
    path('sportman-profile/competitions/<str:pk>', views.sportmanCompetitions, name="sportman-competitions"),
    path('sportman-profile/career/<str:pk>', views.sportmanCareer, name="sportman-career"),
    path('sportman-profile/indicators/<str:pk>', views.sportmanIndicators, name="sportman-indicators"),
    path('sportman-profile/medicine/<str:pk>', views.sportmanMedicine, name="sportman-medicine"),
    path('sportman-profile/diet/<str:pk>', views.sportmanDiet, name="sportman-diet"),
    path('sportman-profile/traumas/<str:pk>', views.sportmanTrauma, name="sportman-traumas"),
]

# Условие для отображения картинкок из бд на локальном сервере
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

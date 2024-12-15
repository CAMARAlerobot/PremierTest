from django.urls import path
from . import views

urlpatterns = [

    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('modifier/', views.modifier_etudiant, name='modifier_etudiant'),
    path('profil/', views.profil, name='profil'),
]

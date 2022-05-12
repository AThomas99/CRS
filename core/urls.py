from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.studentPage, name='studentPage'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('application_status/', views.application_status, name='application_status'),
]

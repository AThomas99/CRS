from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.studentPage, name='studentPage'),
    path('admin_page/', views.adminPage, name='admin'),

    # auth
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),


    path('recommendations/', views.recommendations, name='recommendations'),
    path('personal_info/', views.personalInfo, name='personal_info'),
    path('course_preference/', views.preferencePage, name='preference'),
    path('application_status/', views.application_status, name='application_status'),
]

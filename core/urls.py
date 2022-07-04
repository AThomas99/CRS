from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.studentPage, name='studentPage'),
    path('admin_page/', views.adminPage, name='admin'),

    # auth
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),


    path('course_rating/', views.courseRating, name='course_rating'),
    path('course_recommend/', views.courseRecommendation, name='course_recommend'),
    path('personal_info/', views.personalInfo, name='personal_info'),
    path('course_preference/', views.preferencePage, name='preference'),
    path('application_status/', views.application_status, name='application_status'),
    path('user_profile/', views.userProfilePage, name='user_profile'),


    path('all_applicants/', views.allApplicants, name='all_applicants'),
    path('all_students/', views.allStudents, name='all_students'),
    path('all_courses/', views.allCourses, name='all_courses'),
]

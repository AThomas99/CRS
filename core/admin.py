from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(NectaAPI)

class ApplicationFilter(admin.ModelAdmin):
    list_display=  ("student", "status", "choice1", "choice2", "choice3", "choice4", "choice5", "choice6")

admin.site.register(Application, ApplicationFilter)

class CourseFilter(admin.ModelAdmin):
    list_display=  ("id", "name", "department", "interest", "capacity", "duration")

admin.site.register(Course, CourseFilter)
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    csee = models.CharField(max_length=200, null=False, blank=False)
    acsee = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, unique=True, null=False, blank=False)
    profile_pic = models.ImageField(default="user-1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name


class NectaBasicInfoAPI(models.Model):
    # General Information
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    csee = models.CharField(max_length=200, null=False, blank=False)
    acsee = models.CharField(max_length=200, null=False, blank=False)
    gender = models.CharField(max_length=200, null=False, blank=False)


class NectaCSEEReusltsAPI(models.Model):
    # Results
    physics = models.CharField(max_length=10, null=False, blank=False)
    chemisty = models.CharField(max_length=10, null=False, blank=False)
    biology = models.CharField(max_length=10, null=False, blank=False)
    maths = models.CharField(max_length=10, null=False, blank=False)
    english = models.CharField(max_length=10, null=False, blank=False)


class Department(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False, blank=False)
    capacity = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name
    
    
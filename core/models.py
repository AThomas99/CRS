from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    csee = models.CharField(max_length=200, null=False, blank=False)
    acsee = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=200, unique=True, null=False, blank=False)
    profile_pic = models.ImageField(default="user-1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name


class NectaAPI(models.Model):
    # General Information
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    csee = models.CharField(max_length=200, null=False, blank=False)
    acsee = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=False, blank=False)

    physics = models.CharField(max_length=10, null=True, blank=True)
    chemisty = models.CharField(max_length=10, null=True, blank=True)
    biology = models.CharField(max_length=10, null=True, blank=True)
    maths = models.CharField(max_length=10, null=True, blank=False)
    english = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.first_name +f" "+ self.last_name


class Course(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    department = models.CharField(max_length=200,null=False, blank=False)
    interest = models.CharField(max_length=200, null=True, blank=True)
    capacity = models.IntegerField()
    duration = models.IntegerField()
    requirements = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return str(self.pk)

class Rating(models.Model):
    user=models.ForeignKey(User, related_name='student_rating',on_delete=models.CASCADE,default=None)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,default=None)
    rating=models.CharField(max_length=70)

class Application(models.Model):
    STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )

    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True, related_name='student_course')
    status = models.CharField(max_length=200, choices=STATUS, null=True, blank=True, default='Pending')
    is_open = models.BooleanField(default=True)

    choice1 = models.OneToOneField(Course, on_delete=models.SET_NULL, null=True, related_name='course_choice1')
    choice2 = models.OneToOneField(Course, on_delete=models.SET_NULL, null=True, related_name='course_choice2')
    choice3 = models.OneToOneField(Course, on_delete=models.SET_NULL, null=True, related_name='course_choice3')
    choice4 = models.OneToOneField(Course, on_delete=models.SET_NULL, null=True, related_name='course_choice4')
    choice5 = models.OneToOneField(Course, on_delete=models.SET_NULL, null=True, related_name='course_choice5')
    choice6 = models.OneToOneField(Course, on_delete=models.SET_NULL, null=True, related_name='course_choice6')

    def __str__(self):
        return self.student.first_name + f" " + self.student.last_name 


    

# class Rating(models.Model):
#     user = models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
#     course = models.ForeignKey(Course,on_delete=models.CASCADE,default=None)
#     rating = models.CharField(max_length=70)
#     rated_date = models.DateTimeField(auto_now_add=True)
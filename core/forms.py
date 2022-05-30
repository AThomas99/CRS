# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import *


class CreateStudentForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, label= "First Name",  widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=200, label= "Last Name",  widget=forms.TextInput(attrs={'class':'form-control'}))
    csee = forms.CharField(max_length=200, label= "CSEE Number",  widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=200, label= "Email Address",  widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField( label= "Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField( label= "Password Confirmation", widget=forms.PasswordInput(attrs={'class':'form-control'}))


    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'csee', 'email', 'password1', 'password2', ]


class AddRatingForm(forms.ModelForm):
  
    class Meta:
        model=Rating
        fields=['rating']
        labels={'rating':'Rating'}
        widgets={
            'rating':forms.TextInput(attrs={'type':'range','step':'1','min':'0','max':'5','class':{'custom-range','border-0'}})
        }
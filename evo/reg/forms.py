
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import Profile


class RegisterForm(UserCreationForm):
    Position = (
        ('CEO','CEO' ),
        ('Employee', 'Employee'),
        ('Intern', 'Intern'),
    )
    position = forms.ChoiceField (choices=Position)


    class Meta:
        model = User
        fields = ["username","position","password1","password2"]



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
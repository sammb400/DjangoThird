from django.http import request
from django.shortcuts import render,redirect
from .forms import RegisterForm ,ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
# Register
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            position = form.cleaned_data.get('position')
            messages.success(request, f'Account created for {username}')
            return redirect ('login')
    else:
        form = RegisterForm()
    return render (request, "reg/reg.html", {"form":form})




#Profile
@login_required
def profiles(request):
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES)
        u_form = UserUpdateForm(request.POST, request.FILES)
    else:
        p_form = ProfileUpdateForm()
        u_form = UserUpdateForm()
    context = {'p_form': p_form, 'u_form': u_form}  
    return render (request, "reg/profile.html", context)


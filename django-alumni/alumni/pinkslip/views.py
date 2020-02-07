from django.shortcuts import render, redirect  
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, StudentProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse    
from . models import profile


def login_view(request):
    next = request.GET.get('next')
    form =  UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('profile')    
    context = {
        'form': form,
    }    
    return render(request,'registration/login.html', context)

def Logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def Profile_view(request):
    if (request.user.is_staff):
        stud = request.user.profile
        
        context = {
            'stud': stud
        }

    return render(request, 'student/profileView.html', context)   
    
@login_required
def Profile_Edit_view(request):
       
    profile_instance = request.user.profile
    
    form = StudentProfileForm(request.POST or None, request.FILES, instance=profile_instance)

    if form.is_valid():
        form.save()

    context = {
       'form': form
    }  

    return render(request, 'student/profileEditView.html', context)   






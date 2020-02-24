from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, StudentProfileForm, UserForm
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
        return redirect('profile_edit')    
    context = {
        'form': form,
    }    
    return render(request,'registration/login.html', context)

def Logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def Profile_view(request):
    #\\\\\\\\\\\\\\\\
        suser = request.user
        context = {
            'stud': suser
        }
        return render (request, 'admin/adminView.html', context)
    
@login_required
def Profile_Edit_view(request):
       
    if request.user.is_staff == False:
        profile_instance = get_object_or_404(profile, pk=request.user.profile.id)

        stud = request.user.profile
        last = request.user.last_login

        
        Studform = StudentProfileForm(request.POST, request.FILES, instance=profile_instance)
        user_form = UserForm(request.POST, instance=request.user) 

        if Studform.is_valid() and user_form.is_valid():
            Studform.save()
            user_form.save()
            return redirect('profile')
       

        context = {
            'Studform': Studform,
            'last': last,
            'stud': stud,
            'user_form': user_form
        }      
        return render (request, 'student/profileEditView.html', context)

    else:
        return redirect('profile')





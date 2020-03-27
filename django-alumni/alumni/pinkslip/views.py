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
from . models import profile, User


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
def class_view(request):
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


        
        Studform = StudentProfileForm(request.POST, request.FILES, instance=profile_instance)
        user_form = UserForm(request.POST, instance=request.user) 
        if request.method == 'POST':
            print(Studform.is_valid())
            if user_form.is_valid():
                user_form.save()
                Studform.save()
                print('saved')
                return redirect('class')
            else:
                print('cool')    
        
        else:
            Studform = StudentProfileForm(instance=profile_instance)
            user_form = UserForm(instance=request.user) 

        context = {
            'Studform': Studform,
            'user_form': user_form
        }      
        return render (request, 'student/profileEditView.html', context)

    else:
        return redirect('admin')


@login_required
def admin_view(request):
    if request.user.is_staff:

        users = User.objects.filter(is_staff=False)

        context = {

            'users': users,
        }

        return render(request, 'admin/adminView.html', context)
    else:
        return redirect('profile')    


    


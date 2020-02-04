from django.shortcuts import render, redirect  
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, StudentProfileForm, UserForm


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
        return redirect('home')    
    context = {
        'form': form,
    }    
    return render(request,'registration/login.html', context)




from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    return render(request, 'home.html')


from django.urls import reverse

@login_required
def Profile_view():
    
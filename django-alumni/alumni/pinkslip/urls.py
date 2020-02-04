from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login' ),
    path('home', views.home, name='home'),
    path('profile', views.Profile_view, name='profile'),
]


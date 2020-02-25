from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.login_view, name='login' ),
    path('class', views.class_view, name='class'),
    path('profile', views.Profile_Edit_view, name='profile'),
    path('logout', views.Logout_view, name='logout'),
    path('admin', views.admin_view, name='admin'),
]


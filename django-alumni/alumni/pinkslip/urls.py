from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.login_view, name='login' ),
    path('profile', views.Profile_view, name='profile'),
    path('profile/edit', views.Profile_Edit_view, name='profile_edit'),
    path('logout', views.Logout_view, name='logout')
]


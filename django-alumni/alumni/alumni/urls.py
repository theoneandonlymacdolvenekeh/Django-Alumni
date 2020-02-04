
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
]


# use Include() to add paths from the pinkslip applications
from django.urls import include 

urlpatterns += {
    path('pinkslip/', include('pinkslip.urls')),

}



#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
]   
"""alumni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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

# add URL maps to redirect to the base URL to our application
from django.views.generic import RedirectView
"""
Now let's redirect the root URL of our site (i.e. 127.0.0.1:8000) to the URL 127.0.0.1:8000/catalog/;
this is the only app we'll be using in this project, 
so we might as well. To do this, we'll use a special view function (RedirectView), 
which takes as its first argument the new relative URL to redirect to (/catalog/) 
when the URL pattern specified in the path() function is matched (the root URL, in this case)

"""
urlpatterns += [
    path('', RedirectView.as_view(url='pinkslip/', permanent=True)),
]

"""
implement if this is needed

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
"""mydjangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from newapp.views import data
from newapp.views import generate_PDF
from newapp.views import SaveScreenshot
from newapp.views import emails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', generate_PDF),
    path('', data),
    path('save_screenshot/',SaveScreenshot),
    path('emails/', emails)

]

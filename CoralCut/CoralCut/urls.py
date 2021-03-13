"""CoralCut URL Configuration

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
from CoralCutapp import views
handler404 = 'CoralCutapp.views.handler404'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('coralcut/',views.home_view1),
    path('blackwhite/',views.bandw),
    path('paint/',views.painting),
    path('mirrorx/',views.mirrorx),
    path('mirrory/',views.mirrory),
    path('fadein/',views.fadein),
    path('fadeout/',views.fadeout),
    path('invertcolor/',views.invertcolor),
    path('speedx/',views.speedx),
    path('volumex/',views.volumex),
    path('timesymmetrize/',views.timesymmetrize),
    path('contrast/',views.contrast),
    path('reverse/',views.reverse),
    path('gammacorrection/',views.gammacorrection),
    path('rotate/',views.rotate),
    path('static1/',views.screen1),
    path('subclip/',views.subclip),
    path('evensize/',views.evensize),


]

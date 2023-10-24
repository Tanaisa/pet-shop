"""ultima URL Configuration

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

from django.urls import include

from base.views import inicio
from base.views import contato

app_name = 'rest_api'

from base.views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    path('contato/', contato, name='contato'),
    path('reserva/', include('reserva.urls', namespace='reserva')),
    path('admin/', admin.site.urls),
    

    path('login/', login_usuario, name="login_usuario"),
    path('logout/', logout_usuario, name="logout_usuario"),
    path('cadastro-usuario/', cadastro_usuario,name='cadastro_usuario'),
    path('api_auth/', include("rest_framework.urls")),
    path('api/', include('rest_api.urls',namespace='api')),
]

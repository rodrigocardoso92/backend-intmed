from django.urls import path
from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token

from backend.apps.clientes.views import criar_cliente

urlpatterns = [
    path('api/', criar_cliente),
    path('api/login', obtain_auth_token, name="login")
]

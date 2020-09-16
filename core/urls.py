from django.urls import path
from .views import index, administracao

app_name = 'core'
urlpatterns = [
    path('', index, name="index"),
    path('administracao/', administracao, name="administracao"),
]

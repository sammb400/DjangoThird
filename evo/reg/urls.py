from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.register, name="register"),
    path('prof/', views.profiles, name="profiles"),
]
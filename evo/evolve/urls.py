from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.ev, name="ev"),
    path('upl/', views.upload_file, name="upload_file"), 
]
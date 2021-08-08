from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.ev, name="ev"),
    path('pdf/', views.some_view, name="some_view"),
    path('up/', views.upload, name="upload"), 
    path('upl/', views.upload_file, name="upload_file"), 
]
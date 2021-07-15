from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("<int:id>", views.spe, name="spe"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
]

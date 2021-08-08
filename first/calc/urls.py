from django.urls import path
from . import views

urlpatterns = [
    path ("<int:id>", views.index, name="index"),
    path ("", views.index1, name="index1"),
]

from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreatesNewList

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render (response, "tdl/list.html", {"ls":ls})

 
def home(response):
    return render (response, "tdl/home.html", {})  


def create(response):
    form = CreatesNewList()
    return render (response, "tdl/create.html", {"form":form})  

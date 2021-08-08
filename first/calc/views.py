from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item 

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.all()
    return render (response, "calc/list.html", {"ls":ls})


def index1(response):
    return render (response, "calc/home.html", {})

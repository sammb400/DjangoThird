from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreatesNewList

# Create your views here.



def home(response):
    return render (response, "main/home.html", {})




def spe(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        print (response.POST)
                    #saving an item
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                    item.save()

                    #adding an new item
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt)>2:
                ls.item_set.create(text=txt , complete=False)
            else:
                print("invalid")


    return render (response, "main/list.html", {"ls":ls})
    


def view(response):
    return render (response, "main/view.html", {})


def create(response): 
    t = None
    if response.method == "POST":
        form = CreatesNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

            return HttpResponseRedirect ("/%i" %t.id)
        else:
            return HttpResponseRedirect("/view")

    else:      
        form = CreatesNewList()


    return render (response, "main/create.html", {"form":form})

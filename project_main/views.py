""" from django.http import HttpResponse """
from django.shortcuts import render
from mylist.models import Task

def home(request):
    tasks_not_completed = Task.objects.filter(is_completed = False).order_by("-updated_at")
    """ print(tasks_not_completed) """
    context = {
        "eksik_gorevler" : tasks_not_completed,
    }
    return render(request, "home.html", context= context)
    """ return HttpResponse("<h1>First Wellcome Page</h1>") """
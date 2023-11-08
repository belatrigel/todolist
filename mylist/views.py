from django.shortcuts import redirect, render
from django.http import HttpResponse
from mylist.models import Task

# Create your views here.
def add_task(request):
    gorev = request.POST['task']
    Task.objects.create(task = gorev)
    return redirect('home')

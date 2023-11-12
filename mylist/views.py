from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from mylist.models import Task

# Create your views here.
def add_task(request):
    gorev = request.POST['task']
    Task.objects.create(task = gorev)
    return redirect('home')

def mark_done(request, pk):
    task = get_object_or_404(Task, pk = pk)
    task.is_completed = True
    task.save()
    return redirect("home")

    """ return HttpResponse("yönlendirme yapıldı") """
def mark_undone(request, pk):
    task = get_object_or_404(Task, pk = pk)
    task.is_completed = False
    task.save()
    return redirect("home")

    """ return HttpResponse("yönlendirme yapıldı") """

def editTask(request, pk):
    task = get_object_or_404(Task, pk = pk)
    context = {
        "gorev" : task,
    }
    if request.method == "POST":
        task.task = request.POST["task"]
        task.save()
    return render(request, "edit_task.html", context=context)
    """ return HttpResponse("edit sayfasına gittim") """
def deleteTask(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect("home")
    """ return HttpResponse("silme sayfası") """

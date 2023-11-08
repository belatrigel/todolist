from django.urls import path, include
from mylist import views

app_name = "mylist"

urlpatterns = [
    path("addTak/", views.add_task, name="add_task"),
]

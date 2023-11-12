from django.urls import path, include
from mylist import views

app_name = "mylist"

urlpatterns = [
    path("addTak/", views.add_task, name="add_task"),
    path("markDone/<int:pk>/", views.mark_done, name="mark_done"),
    path("markUndone/<int:pk>/", views.mark_undone, name="mark_undone"),
    path("editTask/<int:pk>/", views.editTask, name="edit_task"),
    path("deleteTask/<int:pk>/", views.deleteTask, name="delete_Task"),
]

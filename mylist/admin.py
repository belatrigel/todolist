from django.contrib import admin
from mylist.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("task", "is_completed", "updated_at",)
    search_fields = ("task", "is_completed",)
# Register your models here.
admin.site.register(Task, TaskAdmin)
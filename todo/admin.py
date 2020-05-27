from django.contrib import admin
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    fields = ['task', 'state', 'deadline']
    list_display = ('task', 'state', 'deadline')

admin.site.register(Task, TaskAdmin)
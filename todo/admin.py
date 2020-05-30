from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Task, ToDoUser

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    fields = ['task', 'state', 'deadline']
    list_display = ('task', 'state', 'deadline')

admin.site.register(ToDoUser, UserAdmin)
admin.site.register(Task, TaskAdmin)

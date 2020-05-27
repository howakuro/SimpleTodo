from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.db.models import F
from django.utils import timezone
from .models import Task
from .forms import TaskForm

# Create your views here.
class IndexView(generic.ListView):
    template_name ='todo/index.html'
    context_object_name= 'latest_todo_list'
    def get_queryset(self):
        return Task.objects.order_by('deadline')

class TaskEditView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('todo:index')

class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name ='todo/task_form.html'
    success_url = reverse_lazy('todo:index')
    def form_valid(self, form):
        result = super().form_valid(form)
        return result
    
    def form_invalid(self, form):
        return super().form_invalid(form)

def task_done(request, todo_id):
    task = get_object_or_404(Task, pk=todo_id)
    task.state = "Done"
    task.save()
    return HttpResponseRedirect(reverse('todo:index',args=()))

def task_delete(request, todo_id):
    task = get_object_or_404(Task, pk=todo_id)
    task.delete()
    return HttpResponseRedirect(reverse('todo:index',args=()))


from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.db.models import F
from django.utils import timezone
from .models import Task, ToDoUser
from .forms import TaskForm, SignUpForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

# Create your views here.
class IndexView(generic.TemplateView):
    template_name ='todo/index.html'
    context_object_name= 'latest_todo_list'

class TasksView(LoginRequiredMixin, generic.ListView):
    template_name ='todo/tasks.html'
    context_object_name= 'latest_todo_list'
    def get_queryset(self):
        user = self.request.user
        return sorted(Task.objects.filter(user_id=user.id).order_by('deadline'), key=lambda task: not task.state_is_done(), reverse=True)

class TaskEditView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('todo:tasks')
    def form_valid(self, form):
        form.instance.user_id = self.request.user
        result = super().form_valid(form)
        return result
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name ='todo/task_form.html'
    success_url = reverse_lazy('todo:tasks')
    def form_valid(self, form):
        form.instance.user_id = self.request.user
        result = super().form_valid(form)
        return result
    
    def form_invalid(self, form):
        return super().form_invalid(form)

@login_required
def task_done(request, todo_id):
    task = get_object_or_404(Task, pk=todo_id)
    task.state = "Done"
    task.save()
    return HttpResponseRedirect(reverse('todo:tasks',args=()))

@login_required
def task_delete(request, todo_id):
    task = get_object_or_404(Task, pk=todo_id)
    task.delete()
    return HttpResponseRedirect(reverse('todo:tasks',args=()))


class SignInView(LoginView):
    form_class = LoginForm
    template_name = 'todo/signin.html'

class SignOutView(LogoutView):
    template_name = 'index.html'

class SineUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'todo/signup.html', {
           "input_error_text": False,
           "form": form,
        })

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            if password1 == password2:
                ToDoUser.objects.create_user(username, email, password1)
                authenticate(username=username, password=password1)
                return render(request, 'todo/signup_ok.html', { })
        return render(request, 'todo/signup.html', {
            "input_error_text": True,
            "from": form
        })

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Task, ToDoUser

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Task
        fields = ('state','task', 'deadline', )
        widgets = {
            'state': forms.RadioSelect(
                # attrs={
                #     "class":"form-check-input",
                # }
            ),
            'task': forms.TextInput(
                attrs={
                    'placeholder':'課題を終わらせる',
                    'class':"form-control",
                }
            ),
            'deadline': forms.DateTimeInput(
                attrs={
                    'placeholder':'2020-05-26 17:45:00',
                    'class':"form-control"
                },
            ),
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label   
            
class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  
    class Meta:
        model = ToDoUser
        fields = ('username', 'email', 'password1', 'password2')
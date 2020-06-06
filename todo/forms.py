from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
import bootstrap_datepicker_plus as datetimepicker
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
            # 'deadline': forms.DateTimeInput(
            #     attrs={
            #         'placeholder':'2020-05-26 17:45',
            #         'class':"form-control"
            #     },
            # ),
            'deadline': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M:%S',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            )
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'
    class Meta:
        model = ToDoUser
        fields = ('username', 'password')
        labels = {
            'username':'Username',
            'password':'Password',
        }

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
        self.fields['username'].label = 'Username'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Password（確認用）'
    class Meta:
        model = ToDoUser
        fields = ('username', 'password1', 'password2')
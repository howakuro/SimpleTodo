from django import forms
from .models import Task

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
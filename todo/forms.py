from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        field_values = list(self.fields.values())
        for field in field_values[1:]:
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Task
        fields = ('state','task', 'deadline', )
        widgets = {
            'state': forms.RadioSelect(),
            'task': forms.TextInput(
                attrs={'placeholder':'課題を終わらせる'}
            ),
            'deadline': forms.DateTimeInput(
                attrs={'placeholder':'2020-05-26 17:45:00'}
            ),
        }
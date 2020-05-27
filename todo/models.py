import datetime

from django.utils import timezone
from django.db import models
from django import forms

# Create your models here.

class Task(models.Model):
    STATE_CHOICES = {
        ("ToDo", "ToDo"),
        ("Do"  , "Do"  ),
        ("Done", "Done"),
    }

    state = models.CharField(
        max_length = 4,
        choices    = STATE_CHOICES,
        default = "ToDo",
    )

    task = models.CharField(max_length=200)
    deadline = models.DateTimeField('deadline')

    def __str__(self):
        return self.task

    def state_is_done(self):
        return self.state == "Done"

    def state_is_do(self):
        return self.state == "Do"
    
    def state_is_todo(self):
        return self.state == "ToDo"
    
    def deadline_exceeded(self):
        return timezone.now() > deadline


    

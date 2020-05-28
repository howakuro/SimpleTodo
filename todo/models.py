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
        """
        stateがdone
        """
        return self.state == "Done"

    def state_is_do(self):
        """
        stateがdo
        """
        return self.state == "Do"
    
    def state_is_todo(self):
        """
        stateがtodo
        """
        return self.state == "ToDo"

    def deadline_exceeded(self):
        """
        deadline（締切）が超過した
        """
        return self.deadline < timezone.now()
    
    def deadline_approaching(self):
        """
        deadline（締切）が近い（後1日で締め切り）
        """
        near_deadline = self.deadline - datetime.timedelta(days=1)
        return near_deadline < timezone.now() < self.deadline


    

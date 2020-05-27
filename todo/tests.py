from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
import datetime

from .models import Task


def create_task(task, state, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Task.objects.create(task=task, state=state, deadline=time)

class TaskModelTests(TestCase):
    def test_status_is_done(self):
        """
        ステータスがdoneであるときtrue
        """
        done_task = Task(state="done")
        self.assertIs(done_task.state_is_done(), True)
    
    def test_status_is_do(self):
        """
        ステータスがdoであるときtrue
        """
        do_task = Task(state="do")
        self.assertIs(do_task.state_is_do(), True)
    
    def test_status_is_not_do(self):
        """
        ステータスがtodoであるときtrue
        """
        todo_task = Task(state="todo")
        self.assertIs(todo_task.state_is_todo(), True) 
        

class TaskIndexViewTests(TestCase):
    def test_no_tasks(self):
        """
        登録されているタスクが無い時に適切な表示が出る。
        """
        response = self.client.get(reverse('todo:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no registered things to do.")
        self.assertQuerysetEqual(response.context['latest_todo_list'], [])
    
    def test_print_task(self):
        """
        タスクが登録されている場合に表示できる
        """
        create_task("task1", "todo", 2)
        response = self.client.get(reverse('todo:index'))
        self.assertQuerysetEqual(response.context['latest_todo_list'], ['<Task: task1>'])

    def test_deadline_orderby_asc(self):
        """
        deadlineが昇順に整列している
        """
        answer_deadline_list = []
        for i in [2, 5, 10]:
            time = timezone.now() + datetime.timedelta(days=i)
            answer_deadline_list.append(time)
        
        for i in [5, 2, 10]:
            create_task("task", "todo", i)

        response = self.client.get(reverse('todo:index'))
        deadline_List = []
        for todo in response.context['latest_todo_list']:
            deadline_List.append(todo.deadline)
        self.assertQuerysetEqual(deadline_List, answer_deadline_list)
        


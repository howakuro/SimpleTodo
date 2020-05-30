from django.urls import path

from . import views


app_name = 'todo'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('tasks', views.TasksView.as_view(), name='tasks'),
    path('create', views.TaskCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.TaskEditView.as_view(), name='edit'),
    path('<int:todo_id>/delete/', views.task_delete, name='delete'),
    path('<int:todo_id>/done/', views.task_done, name='done'),
    path('signup', views.SineUpView.as_view(), name='signup'),
    path('signin', views.SignInView.as_view(), name='signin'),
    path('signout', views.SignOutView.as_view(), name='signout'),

]
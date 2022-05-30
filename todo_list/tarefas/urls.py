from django.urls import path

from todo_list.tarefas import views


app_name = 'tarefas'

urlpatterns = [
    path('', views.home, name='home')
]

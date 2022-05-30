from django.forms import ModelForm

from todo_list.tarefas.models import Tarefa


class TarefaNovaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ('nome', )

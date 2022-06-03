from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from todo_list.tarefas.forms import TarefaNovaForm
from todo_list.tarefas.models import Tarefa


def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
            context = {'form': form,
                       'tarefas_pendentes': tarefas_pendentes
                       }
            return render(request, 'tarefas/home.html', context=context, status=400)

    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
    context = {'tarefas_pendentes': tarefas_pendentes}
    return render(request, 'tarefas/home.html', context=context)

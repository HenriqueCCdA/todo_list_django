from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from todo_list.tarefas.forms import TarefaForm, TarefaNovaForm
from todo_list.tarefas.models import Tarefa


def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
            tarefas_feitas = Tarefa.objects.filter(feita=True).all()
            context = {'form': form,
                       'tarefas_pendentes': tarefas_pendentes,
                       'tarefas_feitas': tarefas_feitas
                       }
            return render(request, 'tarefas/home.html', context=context, status=400)

    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
    tarefas_feitas = Tarefa.objects.filter(feita=True).all()
    context = {'tarefas_pendentes': tarefas_pendentes,
               'tarefas_feitas': tarefas_feitas
               }
    return render(request, 'tarefas/home.html', context=context)


def detalhe(request, tarefa_id):
    if request.method == 'POST':
        tarefa = Tarefa.objects.get(id=tarefa_id)
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse('tarefas:home'))


def apagar(request, tarefa_id):
    if request.method == 'POST':
        Tarefa.objects.filter(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('tarefas:home'))

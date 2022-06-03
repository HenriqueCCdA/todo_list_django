from http import HTTPStatus

from django.urls import reverse
import pytest
from pytest_django.asserts import assertContains

from todo_list.tarefas.models import Tarefa


@pytest.fixture
def resposta(client, db):
    return client.get(reverse('tarefas:home'))


def test_status_code(resposta):
    assert resposta.status_code == HTTPStatus.OK


def test_formulario_presente(resposta):
    assertContains(resposta, '<form')


def test_botao_salvar_presente(resposta):
    assertContains(resposta, '<button type="submit"')


@pytest.fixture
def lista_de_tarefas_pendentes(db):
    tarefas = [
            Tarefa(nome='Tarefa 1', feita=False),
            Tarefa(nome='Tarefa 2', feita=False),
    ]
    Tarefa.objects.bulk_create(tarefas)

    return tarefas


@pytest.fixture
def resposta_com_lista_de_tarefas(client, lista_de_tarefas_pendentes):
    return client.get(reverse('tarefas:home'))


@pytest.fixture
def lista_de_tarefas_feitas(db):
    tarefas = [
            Tarefa(nome='Tarefa 3', feita=True),
            Tarefa(nome='Tarefa 4', feita=True),
    ]
    Tarefa.objects.bulk_create(tarefas)

    return tarefas


@pytest.fixture
def resposta_com_lista_de_tarefas_feitas(client, lista_de_tarefas_feitas):
    return client.get(reverse('tarefas:home'))


def test_lista_de_tarefas_pendentes_presentes(resposta_com_lista_de_tarefas, lista_de_tarefas_pendentes):
    for tarefa in lista_de_tarefas_pendentes:
        assertContains(resposta_com_lista_de_tarefas, tarefa.nome)


def test_lista_de_tarefas_feitas_presentes(resposta_com_lista_de_tarefas_feitas, lista_de_tarefas_feitas):
    for tarefa in lista_de_tarefas_feitas:
        assertContains(resposta_com_lista_de_tarefas_feitas, tarefa.nome)

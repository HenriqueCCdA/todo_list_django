from http import HTTPStatus
import pytest

from django.urls import reverse
from todo_list.tarefas.models import Tarefa


@pytest.fixture
def resposta(client, db):
    return client.post(reverse('tarefas:home'), data={'nome': 'Tarefa'})


def test_tareda_existe_no_db(resposta):
    assert Tarefa.objects.exists()


def test_redirecionamento_depois_do_salvamento(resposta):
    assert resposta.status_code == HTTPStatus.FOUND


@pytest.fixture
def resposta_dado_invalido(client, db):
    return client.post(reverse('tarefas:home'), data={'nome': ''})


def test_tarefa_nao_existe_no_db(resposta_dado_invalido):
    assert not Tarefa.objects.exists()


def test_pagino_com_dados_incalidos(resposta_dado_invalido):
    assert resposta_dado_invalido.status_code == HTTPStatus.BAD_REQUEST

from http import HTTPStatus

from django.test import Client


def test_home(client: Client):
    reposta = client.get('/')
    assert reposta.status_code == HTTPStatus.OK

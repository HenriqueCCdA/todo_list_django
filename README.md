# todo_list_django
Projeto to do list da dev pro.

## Deploy

### Criando o projeto no heroku

```console
heroku create django-todo-list-hcca
```

### Gerando a chave secreta

```console
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

```console
heroku config:set DISABLE_COLLECTSTATIC=1
heroku config:set DEBUG=FALSE
```

### Deploy manual para heroku

```console
git push heroku main
```

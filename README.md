# django_training - Eventex
    Sistema de eventos

## Basic configs (unix)
    - alias manage='python $VIRTUAL_ENV/../manage.py'

## Heroku
    - heroku login
    - git push heroku main --force

## Run
    - Clone o repositório
    - Crie um ambiente virtual com python 3.8
    - Ative o ambiente virtual
    - instale as dependências
    - Configure a instância com o .env
    - Execute os testes

```console
    git clone https://github.com/Mrpsousa/django_training_WD
    cd django_training_WD
    sudo pip3 install virtualenv 
    sudo virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    cp contrib/env-sample .env
    python manage.py test
    python manage.py runserver
```
## Deploy
    - Crie uma instância no heroku
    - Envie as configurações para o heroku
    - Defina uma SECRET_KEY segura para instância
    - Defina DEBUG=False
    - Configure o serviço de email
    - Envie o código para o heroku

```console
    heroku create nome_da_instância
    heroku config:push
    heroku config:set SECRET_KEY = 'python contrib/secret_gen.py'
    heroku config:set DEBUG=false
    # configura o email
    git push heroku master/main --force
```

### Attention
    - python3 manage.py collectstatic
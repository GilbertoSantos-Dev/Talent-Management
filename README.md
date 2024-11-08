# talent-management

## versão 1.0
    - Esta versão está sem o Docker
    - Na próxima versão este código será convertivo para dentro de um container Docker

## Instalação
Todos estes itens abaixo devem ser executados no terminal
    - Após clonado o repositório, crie uma venv
    - Ative a venv que foi criada
    - execute 
        - pip install -r .\requirements.txt
        - python manage.py makemigrations 
        - python manage.py migrate

## Configurações Iniciais
Todos estes itens abaixo devem ser executados no terminal
    - crie um usuário administrador, para isto execute 
        - python manage.py createsuperuser
        - Responda as perguntas que irão aparecer no terminal (nome de usuário, e-mail e senha)
    - crie um usuário administrador, para isto execute
        - python manage.py shell
        - from django.contrib.auth.models import User
        - User.objects.create_user(username='usuario_comum', password='senha_segura', email='usuario@exemplo.com') 
          defina seu 'usuario_comum', 'senha_segura' e 'usuario@exemplo.com'
        - exit()

## Executando o Projeto
Todos estes itens abaixo devem ser executados no terminal
    - python manage.py runserver

## Testando as rotas com Swagger
No navegador acesse http://127.0.0.1:8000/swagger/


# Livraria Online - TSMX

Este é um projeto-desafio da empresa TSMX construído com Django, utilizando PostgreSQL como banco de dados e integrando a API do Google Books para buscar e exibir informações de livros. O front-end é construído com HTML e CSS.

## Tecnologias Utilizadas

 - Python (versão 3.12.6)
 - Django (versão 5.1.1)
- PostgreSQL (versão 8.12)
- Google Books API
- HTML (estrutura da página)
- CSS (estilização)


## Funcionalidades

- Busca de livros via Google Books API. (OK)
- Visualização detalhada dos livros. (OK)
- Sistema de usuários com autenticação (login e cadastro). (OK)
- Carrinho de compras.


## Instalação

Antes de começar, você precisará ter instalado:

- Python 3.12 ou superior
- PostgreSQL (versão 12 ou superior)
- Virtualenv (opcional, mas recomendado)
- Google Books API
- Você precisará de uma chave de API da Google Books. Veja como obter uma chave de API aqui.

## Passo a Passo de Instalação
1. Clone o repositório

```bash
  git clone https://github.com/seu-usuario/livraria-online-tsmx.git
  cd livraria-online-tsmx
```
    
1. Crie e ative um ambiente virtual

No Windows:

```bash
  python -m venv env
  env\Scripts\activate 
```

No Linux ou macOS:

```bash
  python3 -m venv env
  source env/bin/activate
```

3. Instale as dependências
Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
  pip install -r requirements.txt
```

4. Configurar o PostgreSQL

Crie um banco de dados no PostgreSQL:

```bash
CREATE DATABASE livraria_online;
CREATE USER livraria_user WITH PASSWORD 'sua_senha';
ALTER ROLE livraria_user SET client_encoding TO 'utf8';
ALTER ROLE livraria_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE livraria_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE livraria_online TO livraria_user;
```

No arquivo settings.py, configure a conexão com o banco de dados:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'livraria_online',
        'USER': 'livraria_user',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. Configurar a Google Books API

No arquivo settings.py, adicione a sua chave de API do Google Books:

```bash
GOOGLE_BOOKS_API_KEY = 'sua_chave_de_api_aqui'
```

6. Aplicar as migrações

Agora que o banco de dados está configurado, aplique as migrações para criar as tabelas:

```bash
python manage.py makemigrations
python manage.py migrate
```

7. Criar um superusuário

Para acessar o painel de administração do Django, crie um superusuário:

```bash
python manage.py createsuperuser
```

8. Rodar o servidor
Finalmente, execute o servidor local do Django:

```bash
python manage.py runserver
```

Acesse o projeto em http://127.0.0.1:8000.

Próximos Passos
Acesse o painel administrativo: http://127.0.0.1:8000/admin
Cadastre usuários e adicione livros ao carrinho.
## Autores

- [@geovanesilvahr](https://github.com/geovanesilvahr)

 "Quero agradecer a oportunidade de desenvolver esse projeto incrível. É projetos como esse que me encantam e alimentam minha paixão pela programação. Mesmo não conseguido finalizar todos os requisitos até o prazo limite, continuarei estudando e aperfeiçoando esse projeto. Muito obrigado." - Geovane Silva

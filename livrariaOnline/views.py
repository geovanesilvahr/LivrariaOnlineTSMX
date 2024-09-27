import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Book, PurchasesMade
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def homeSearch(request):
    query = request.GET.get('q', '')
    api_key = 'AIzaSyCLxUPoZrcqnEixqyR1uek--0jYNS_lmBU'
    books = []

    if query:
        url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            books = data.get('items', [])
            print(books)

    return render(request, 'homeSearch.html', {'books': books})

@csrf_protect
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(username=name, password=password)

        if user:
            return HttpResponse('Autenticado!')
        else: 
            return HttpResponse('Usuario e/ou Senha invalida!')

@csrf_protect
def createUser(request):
    if request.method == "GET":
        return render(request, 'createUser.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('passwords')

        user = User.objects.filter(username=name).first()

        if user:
            return HttpResponse('Já existe esse usuário')

        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        
        return HttpResponse("Usuario Cadastrado com Sucesso!")

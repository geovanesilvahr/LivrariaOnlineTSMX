import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Book, User, PurchasesMade


def index(request):
    books = Book.objects.all()
    return render(request, "index.html", {'books': books})

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

def login(request):
    return render(request, 'login.html')

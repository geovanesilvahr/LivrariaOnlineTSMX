import requests
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from livrariaOnline.models import Book, Cart


def homeSearch(request):
    query = request.GET.get("q", "")
    api_key = "AIzaSyCLxUPoZrcqnEixqyR1uek--0jYNS_lmBU"
    books = []

    if query:
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            books = data.get("items", [])

    return render(request, "homeSearch.html", {"books": books})


@csrf_protect
def loginUser(request):
    error_message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "cartView.html")
        else:
            return render(
                request, "loginUser.html", {"error": "Usuário e/ou senha inválidos."}
            )

    return render(request, "loginUser.html")


@csrf_protect
def createUser(request):
    if request.method == "GET":
        return render(request, "createUser.html")
    else:
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(username=name).first()

        if user:
            return HttpResponse("Já existe esse usuário")

        user = User.objects.create_user(username=name, email=email, password=password)
        user.set_password = password
        user.save()

        return HttpResponse("Usuario Cadastrado com Sucesso!")


def bookView(request, book_id):

    response = requests.get(f"https://www.googleapis.com/books/v1/volumes/{book_id}")
    book = response.json()

    return render(request, "bookView.html", {"book": book})


"""
def cartView(request):
   
    cart_id = request.session.get("cart_id", None)
    if cart_id in None:
        print("Create New Cart")
        request.session["cart_id"] = 12
    else:
        print("Cardt ID Exists")
    return render(request, "cartView.html")

def cartAdd(request, book_id):
    request.session['books'] = book_id
    print( request.session['books'])
    return HttpResponse(request.session['books'])
"""


def cartAdd(request, book_id):
    if request.user.is_authenticated:
        user = request.user
        book = get_object_or_404(Book, id=book_id)  # Obtém o objeto Book

        cart_item, created = Cart.objects.get_or_create(user=user, book=book)

        if not created:
            cart_item.quantity += (
                1  # Incrementa a quantidade se o item já estiver no carrinho
            )
            cart_item.save()

        return HttpResponse(
            f"Added Book ID: {book_id} to cart. Quantity: {cart_item.quantity}"
        )
    else:
        return HttpResponse(
            "You need to be logged in to add items to the cart.", status=401
        )

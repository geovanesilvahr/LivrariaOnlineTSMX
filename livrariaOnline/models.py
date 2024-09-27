from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=90)
    date_publication = models.DateField()
    front_book = models.ImageField()
    synopsis = models.TextField()
    pages = models.IntegerField()
    publisher = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.title

class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class PurchasesMade(models.Model):
    id_user = models.ForeignKey("User", on_delete=models.CASCADE)
    books_list = models.TextField()

    def __str__(self) -> str:
        return self.id_user

class CartItens(models.Model):
    list_itens = models.TextField()
    total_price = models.FloatField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
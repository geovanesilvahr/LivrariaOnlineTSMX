from django.db import models
from django.conf import settings

class Book(models.Model):
    book_id = models.CharField(max_length=30)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=90)
    date_publication = models.DateField()
    front_book = models.ImageField(upload_to='')
    synopsis = models.TextField(default='')
    pages = models.IntegerField(default=1)
    publisher = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.title

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
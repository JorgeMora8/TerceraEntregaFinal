from django.db import models

# Create your models here.
class Product(models.Model): 
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    on_sale = models.BooleanField(default=True)
    inventory = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self): 
        return self.name

class User(models.Model): 
    name = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    email = models.EmailField(max_length=154)
    proffesion = models.TextField(max_length=50, null=True)

    def __str__(self): 
        return f"{self.name}"
    
class Review(models.Model): 
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=150)

    def __str__(self): 
        return f"{self.name} {self.text[0:20]}..."


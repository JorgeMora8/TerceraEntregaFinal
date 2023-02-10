from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Another message
def homepage(request): 
    return render (request,'homepage.html')

def products(request): 
    return render (request, 'products.html')

def reviews(request): 
    return render(request, 'reviews.html')
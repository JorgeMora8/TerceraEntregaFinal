from django.shortcuts import render
from .Services import home_page_logic, product_page_logic, reviews_page_logic

def homepage(request): 
    context = home_page_logic(request)
    return render (request,'homepage.html', context)

def products(request): 
    context = product_page_logic(request)
    return render (request, 'products.html', context)

def reviews(request): 
    context = reviews_page_logic(request)
    return render(request, 'reviews.html', context)
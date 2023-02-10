from django.shortcuts import render, redirect
from django.http import HttpResponse

#Importacion de formularios para agregar datos
from .forms.userForm import UserForm
from .forms.reviewForm import ReviewForm
from .forms.productForm import ProductForm
from .models import Product, Review, User

# Create your views here.
#Another message
def homepage(request): 
    userList = User.objects.all()
    form = UserForm()
    if request.method == 'POST': 
        form = UserForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('store')
    
    context = {"form": form, "users": userList}
    return render (request,'homepage.html', context)

def products(request): 

    
    productList = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST': 
        form = ProductForm(request.POST)
        if form.is_valid(): 
            form.save()
            redirect("store")
    
    if request.method == 'GET': 
        print(request.GET)

    context = {"form": form, "products": productList}
    return render (request, 'products.html', context)

def reviews(request): 
    reviewList = Review.objects.all()
    form = ReviewForm()
    if request.method == "POST": 
        form = ReviewForm(request.POST)
        if form.is_valid(): 
            form.save()
            redirect('store')

    context = {"form": form, "reviews": reviewList}
    return render(request, 'reviews.html', context)
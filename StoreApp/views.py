from django.shortcuts import render, redirect
from django.http import HttpResponse

#Importacion de formularios para agregar datos
from .forms.userForm import UserForm
from .forms.reviewForm import ReviewForm
from .forms.productForm import ProductForm

# Create your views here.
#Another message
def homepage(request): 
    form = UserForm()
    if request.method == 'POST': 
        form = UserForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('store')
    
    context = {"form": form}
    return render (request,'homepage.html', context)

def products(request): 
    form = ProductForm()
    if request.method == 'POST': 
        form = ProductForm(request.POST)
        if form.is_valid(): 
            form.save()
            redirect("store")

    context = {"form": form}
    return render (request, 'products.html', context)

def reviews(request): 
    form = ReviewForm()
    if request.method == "POST": 
        form = ReviewForm(request.POST)
        if form.is_valid(): 
            form.save()
            redirect('store')

    context = {"form": form}
    return render(request, 'reviews.html', context)
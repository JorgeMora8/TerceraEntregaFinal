from django.shortcuts import render, redirect
from django.http import HttpResponse

#Importacion de formularios para agregar datos
from .forms.userForm import UserForm
from .forms.reviewForm import ReviewForm
from .forms.productForm import ProductForm
from .models import Product, Review, User, type_of_product

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
    q = request.GET.get('q')
    productTypeList = type_of_product.objects.all()

    if q == None: 
            productList = Product.objects.all()
    else: 
        productList = Product.objects.filter(type__type=q)
    
    form = ProductForm()
    if request.method == 'POST': 
        form = ProductForm(request.POST)
        if form.is_valid(): 
            form.save()
            redirect("store")
    
    if request.method == 'GET': 
        print(request.GET)

    context = {"form": form, "products": productList, "type_list":productTypeList}
    return render (request, 'products.html', context)

def reviews(request): 
    q = request.GET.get("q")

    if q == None:
        reviewList = Review.objects.all()
    else: 
        reviewList = Review.objects.filter(name__name = q)
        if reviewList.__len__() == 0:
            reviewList = None

    users= User.objects.all()
    
    form = ReviewForm()
    if request.method == "POST": 
        form = ReviewForm(request.POST)
        if form.is_valid(): 
            form.save()
            redirect('store')


    context = {"form": form, "reviews": reviewList, "users": users}
    return render(request, 'reviews.html', context)
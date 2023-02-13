from django.shortcuts import redirect

#Forms
from .forms.userForm import UserForm
from .forms.reviewForm import ReviewForm
from .forms.productForm import ProductForm

#Database management
from .DDBB.DAOsqlite import dao_products, dao_user, dao_product_type, dao_reviews

def home_page_logic(req): 
    users = dao_user.get_all()
    form = UserForm()
    if req.method == 'POST': 
        form = UserForm(req.POST)
        if form.is_valid(): 
            form.save()
            # return redirect('store')
    
    return {"form": form, "users": users}

def product_page_logic(request): 
    query = request.GET.get('q')
    productTypeList = dao_product_type.get_all()
    
    if query == None: 
        productList = dao_products.get_all()
    else: 
        productList = dao_products.get_by_type(query)
    
    form = ProductForm()
    if request.method == 'POST': 
        form = ProductForm(request.POST)
        if form.is_valid(): 
            form.save()
            # redirect("store")

    context = {"form": form, "products": productList, "type_list":productTypeList}
    return context    
    

def reviews_page_logic(req): 
    query = req.GET.get("q")

    if query == None:
        reviews = dao_reviews.get_all()
    else: 
        reviews = dao_reviews.get_by_name(query)
        if reviews.__len__() == 0:
            reviews = None

    users = dao_user.get_all()
    
    form = ReviewForm()
    if req.method == "POST": 
        form = ReviewForm(req.POST)
        if form.is_valid(): 
            form.save()
            # redirect('store')


    return {"form": form, "reviews": reviews, "users": users}
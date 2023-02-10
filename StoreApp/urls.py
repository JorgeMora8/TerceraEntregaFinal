from django.urls import path
from .views import *


urlpatterns = [
    path("store/", homepage, name="store"), 
    path("products/", products, name="products"), 
    path("reviews/", reviews, name="review"),
]
from django.urls import path
from .views import *


urlpatterns = [
    path("", homepage, name="store"), 
    path("products/", products, name="products"), 
    path("reviews/", reviews, name="review"),
]
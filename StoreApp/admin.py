from django.contrib import admin
from .models import *

# Register your models here.
#Adding the models
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Review)

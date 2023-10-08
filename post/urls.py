
from django.urls import path
from .views import *

urlpatterns = [
    
    path('', homepage,name ='home'),
    path('cart/', cartpage,name ='cart'),
    path('checkout/', checkpage,name ='checkout'),
    path('contact/', contactpage,name ='contact'),
    path('product/<int:id>', detailpage,name ='detail'),
    path('shop/', shoppage,name ='shop'),
    path('phone/add/',post_create_phone,name='phoneadd')
]
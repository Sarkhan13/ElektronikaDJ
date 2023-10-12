
from django.urls import path
from .views import *

urlpatterns = [
    
    path('', homepage,name ='home'),
    path('cart/', cartpage,name ='cart'),
    path('checkout/', checkpage,name ='checkout'),
    path('contact/', contactpage,name ='contact'),
    path('product/<int:id>', detailpage,name ='detail'),
    path('shop/', shoppage,name ='shop'),
    path('phone/add/',post_create_phone,name='phoneadd'),
    path('note/add/',post_create_note,name='noteadd'),
    path('phone/<int:id>/update', post_update_phone, name='phoneupdate'),
    path('post/<int:id>/delete', post_delete, name='postdelete'),

]
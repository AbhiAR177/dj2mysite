from django.urls import path,include
from .views import ProductDetailView, ProductListView,index,new_one,add_product, update_product,delete_product,add_to_cart,show_cart

app_name = 'myapp'

urlpatterns = [
    path('',index),
    path('new/',new_one),
    path('products/',ProductListView.as_view(),name='products'),
    path('products/<int:pk>',ProductDetailView.as_view(),name='product_details'),
    path('products/add',add_product,name='add_product'),
    path('products/update/<int:id>',update_product,name='update_product'),
    path('products/delete/<int:id>',delete_product,name='delete_product'),
    path('products/add-to-cart/',add_to_cart, name='add-to-cart'),
    path('products/cart/',show_cart, name='showcart'),
    # path('products/checkout/',show_cart, name='checkout')
    
]

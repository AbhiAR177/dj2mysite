from django.urls import path,include
from .views import index,new_one,products


urlpatterns = [
    path('',index),
    path('new',new_one),
    path('products',products)
    
]

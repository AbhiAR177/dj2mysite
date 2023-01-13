from django.contrib import admin

from myapp.models import ProductModel
from myapp.models import Cart


# Register your models here.

admin.site.register(ProductModel)


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['name','id','price','description',]


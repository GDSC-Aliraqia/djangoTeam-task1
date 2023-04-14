from django.contrib import admin
<<<<<<< HEAD
from library.models import BookAuth, Product
=======
from library.models import *
>>>>>>> 14fce27 (mytask)

# Register your models here.

@admin.register(Product)
<<<<<<< HEAD
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','is_active','is_rare','is_DrawTool']


@admin.register(BookAuth)
class BookAuthAdmin(admin.ModelAdmin):
    list_display = ['id','name','email']

=======
class BooksAdmin(admin.ModelAdmin):
    list_display = ['name','P_id']
    

@admin.register(BookAuth)
class authAdmin(admin.ModelAdmin):
    list_display = ['name']
>>>>>>> 14fce27 (mytask)

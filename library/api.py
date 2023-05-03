from ninja import NinjaAPI
from ninja import Router
from .models import Product, BookAuth
from .schemas import *
from django.shortcuts import get_object_or_404
from typing import List

auth_router = Router(tags=['auth'])
pr_router = Router(tags=['produc'])


#Endpoint To Get All Available Books.
@pr_router.get('Display_available_books', response=List[ProductOut])
def display_all_books(request):
    products = Product.objects.all().filter(is_DrawTool = False)
    books = products.filter(is_active = True)
    return products


#Endpoint To Get Book With ID
@pr_router.get('book_id', response= List[ProductOut])
def book_id(request, book_id: int):
    product = Product.objects.all().filter(id = book_id)
    return product


#Endpoint To Get Auth With Specific Name.
@auth_router.get('Authname', response= List[AuOut])
def Authname(request, Authname: str):
    bookAuth = BookAuth.objects.all().filter(name = Authname)
    return bookAuth


#Endpoint To Create a book
@pr_router.post('create_book')
def create_book(request, data: ProductIn):
    new_product = Product.objects.create(**data.dict())
    return "Book has been successfully created"

#Endpoint To Delete a book
@pr_router.delete('delete_book')
def delete_book(request, book_id:int):
    delete_book = get_object_or_404(Product, id = book_id)
    delete_book.delete()
    return "Book has been successfully deleted"

#Endpoint To Create an auth
@auth_router.post('create_auth')
def create_auth(request, data: AuthOut):
    new_auth = BookAuth.objects.create(**data.dict())
    return "Auth has been successfully created"

#Endpoint To Delete an auth
@auth_router.delete('delete_auth')
def delete_auth(request, auth_id:int):
    delete_auth = get_object_or_404(BookAuth, id = auth_id)
    delete_auth.delete()

    return "Auth has been successfully deleted"

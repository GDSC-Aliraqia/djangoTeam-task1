from typing import List
from ninja import Router
from library.models import *
from library.schemas import MassageOut, ProductOut


product_router = Router(tags=['Product'])

@product_router.get('Display_all_books', response={
    200: List[ProductOut],
    404: None
})
def display_all_books(request):
    products = Product.objects.all().filter(is_DrawTool = False)

    if not products:
        return 404, None
    return 200, products



#Endpoint To Get All Available Books
@product_router.get('Display_avialable_books', response={
    200: List[ProductOut],
    404: None
})
def display_avialable_books(request):
    products = Product.objects.filter(is_DrawTool = True)
    books = products.filter(is_active = True)

    if not books:
        return 404,None
    return 200, books


#Endpoint To Get Book With ID
@product_router.get('display_book', response={
    200:ProductOut,
    404: None
})
def display_book(request , book_id: int):
    product = Product.objects.get(id = book_id)
    if not product:
        return 404,None
    return 200,product

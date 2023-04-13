from ninja import NinjaAPI
from ninja import Router
from .models import Product, BookAuth


Pr_Router = Router(tags=["Produc"])
Ath_Router = Router(tags=["book_Auth"])


@Pr_Router.get("hi")
def hi(request):
    num1 = 2
    num2 = 3
    sum = num1 + num2
    return {"Sum" : sum}

# EndPoint to Get All Available Books
@Pr_Router.get("Books")
def books(request):
    books_list = []
    product = Product.objects.all()
    for book in product:
        if book.is_DrawTool == False and book.is_active == True:
            books_list.append(book)
    return [{"book_name": b.name, "book_price": b.price, "book_auth": b.book_auth} for b in books_list]

#Endpoint To Get Book With ID
@Pr_Router.get("/{book_id}")
def specific_book(request, book_id: int):
    books_list = []
    product = Product.objects.get(id=book_id)
    for book in product:
        if book.is_DrawTool == False:
            books_list.append(book)
    return [{"book_name": b.name, "book_price": b.price, "book_auth": b.book_auth} for b in books_list]


@Ath_Router.get("hello")
def hello(request):
    return None

#Endpoint To Get Auth With Specific Name
@Ath_Router.get("Auth/{auth_name}")
def auth(request, auth_name):
    auth_list = BookAuth.objects.get(name=auth_name)
    return [{"auth_name": auth.name, "auth_email": auth.email,}for auth in auth_list]


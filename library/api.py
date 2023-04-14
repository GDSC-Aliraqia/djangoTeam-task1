from ninja import NinjaAPI
from ninja import Router

from .models import Product, BookAuth


Pr_Router = Router(tags=["Produc"])
Ath_Router = Router(tags=["book_Auth"])


@Pr_Router.get("hi")



from .models import BookAuth,Product

# 1- Endpoint To Get All Available Books.

# 2- Endpoint To Get Book With ID.

# 3- Endpoint To Get Auth With Specific Name.

# 4- According To Your Opinion،  Complete The Relationship Between Product & BookAuth Models.


Pr_Router = Router(tags=["Product"])

Ath_Router = Router(tags=["Product"])

api=Router(tags=["Product"])

@Pr_Router.get("books")

def hi(request):
    return Product.objects.filter(is_active__exact=True)

<<<<<<< HEAD
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



@Ath_Router.get("book&id")
def hello(request):
    x=Product.objects.all()
    return x.name,x.P_id

@api.get("bookauth")
def auth(request,name):

    return name


    return BookAuth.objects.get(name="IDK!")


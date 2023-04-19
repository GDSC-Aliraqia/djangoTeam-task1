from ninja import NinjaAPI
from ninja import Router
from .models import Product, BookAuth
from ninja import Schema

# making schema
# book schema
class BookIn(Schema):
    book_auth: int = None
    name: str
    price: str
    image: str = None

#Auth schema
class AuthIn(Schema):
    name: str
    email: str = None
    phone: int
    number_of_book: int



Pr_Router = Router(tags=["Produc"])
Ath_Router = Router(tags=["book_Auth"])

# Create api for books
@Pr_Router.post("create Book")
def create_book(request, payload: BookIn):
    book = Product.objects.create(**payload.dict())
    return {"id": book.id}
# Update api for books
@Pr_Router.put("Update Book/{book_id}")
def update_book(request, book_id: int, payload: BookIn):
    book = Product.objects.get(id=book_id)
    for attr, value in payload.dict().items():
        setattr(book, attr, value)
    book.save()
    return {"success": True}
# Delete api for books
@Pr_Router.delete("delete book/{book_id}")
def delete_bok(request, book_id: int):
    book = Product.objects.get(id=book_id)
    book.delete()
    return {"success": True}

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
    auth_list = BookAuth.objects.filter(name=auth_name)
    return [{"auth_name": auth.name, "auth_email": auth.email,}for auth in auth_list]
# Create api for Auth
@Ath_Router.post("create Auth")
def create_auth(request, payload: AuthIn):
    book_aut = BookAuth.objects.create(**payload.dict())
    return {"id": book_aut.id}
# Update api for Auth
@Ath_Router.put("Update Auth/{auth_id}")
def update_auth(request, auth_id: int, payload: AuthIn):
    book_auth = BookAuth.objects.get(id=auth_id)
    for attr, value in payload.dict().items():
        setattr(book_auth, attr, value)
    book_auth.save()
    return {"success": True}
# Delete api for Auth
@Ath_Router("Delete Auth/{auth_id}")
def delete_auth(request, auth_id: int):
    book_auth = BookAuth.objects.get(id=auth_id)
    book_auth.delete()
    return {"success": True}
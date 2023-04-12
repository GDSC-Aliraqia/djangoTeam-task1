from ninja import NinjaAPI
from ninja import Router


Pr_Router = Router(tags=["Produc"])
Ath_Router = Router(tags=["book_Auth"])


@Pr_Router.get("hi")
def hi(request):
    num1 = 2
    num2 = 3
    sum = num1 + num2
    return {"Sum" : sum}


@Ath_Router.get("hello")
def hello(request):
    return None

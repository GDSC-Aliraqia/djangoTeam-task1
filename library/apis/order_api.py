from typing import List
from ninja import Router
from library.models import *
from library.schemas import OrderOut

order_router = Router(tags=["Orders"])

@order_router.get("display_order", response={
    200: List[OrderOut],
    404: None})
def display_order(request):
    try:
        orders = Cart.objects.all()
        return 200, orders
    except:
        return 404, None
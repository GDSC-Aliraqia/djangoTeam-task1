from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404
from library.models import *
from library.schemas import CartOut, CartIn

cart_router = Router(tags=["Carts"])


@cart_router.get("display_car", response={
    200: List[CartOut],
    404: None})
def display_car(request, user_name: str):
    try:
        carts = Cart.objects.filter(user=user_name)
        return 200, carts
    except:
        return 404, None


@cart_router.put("/carts/{cart_id}", response={200: CartOut})
def update_cart(request, cart_id: int, payload: CartIn):
    cart = get_object_or_404(Cart, id=cart_id)
    for attr, value in payload.dict().items():
        setattr(cart, attr, value)
    cart.save()
    return {"success": True}


@cart_router.delete("carts/{card_id}")
def delete_cart(request, cart_id: int):
    cart = get_object_or_404(Cart, id=cart_id)
    cart.delete()
    return {"success": True}



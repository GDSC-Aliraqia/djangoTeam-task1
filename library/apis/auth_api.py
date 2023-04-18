from typing import List
from ninja import Router
from library.models import *
from django.db.models import Q
from library.schemas import AuthOut

auth_router = Router(tags=['Book_Auth'])


#Endpoint To Get Auth With Specific Name
@auth_router.get('display_auth', response={
    200: List[AuthOut],
    404: None
    })
def display_auth(request , auth_name: str ):
    auths = BookAuth.objects.all()
    auths = auths.filter(
        Q(name__icontains = auth_name)
    )
    if not auths:
        return 404, None
    return 200, auths


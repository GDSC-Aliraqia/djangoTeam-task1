"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
<<<<<<< HEAD

=======
from library.views import MyModelList
>>>>>>> 14fce27 (mytask)
from library.api import Ath_Router, Pr_Router

api = NinjaAPI()

api.add_router('Product', Pr_Router)
api.add_router('Book_Auth', Ath_Router)
<<<<<<< HEAD

urlpatterns = [
=======
# name='my-model-list'
urlpatterns = [
    path('mymodels/', MyModelList.as_view(), ),
>>>>>>> 14fce27 (mytask)
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]

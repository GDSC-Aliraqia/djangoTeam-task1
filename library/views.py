<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from rest_framework import generics
from .models import BookAuth,Product
from .serializers import MyModelSerializer


class MyModelList(generics.ListAPIView):
    tast1=Product.objects.all()
   # task2 = Product.objects.get(name="name")
    task3=BookAuth.objects.all()
    serializer_class = MyModelSerializer
>>>>>>> 14fce27 (mytask)

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializer import *


# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class NewProductViewSet(ModelViewSet):
    queryset = NewProduct.objects.all()
    serializer_class = NewProductSerializer
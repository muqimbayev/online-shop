from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class UsersView(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
   
class MahsulotView(ModelViewSet):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer
   
class BuyurtmaView(ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer
   
class ChegirmaView(ModelViewSet):
    queryset = Chegirma.objects.all()
    serializer_class = ChegirmaSerializer
   

from rest_framework import serializers
from .models import Buyurtma, Mahsulot, Chegirma, Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('nomi', 'telefon_raqami')

class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'
        read_only_fields = ['narxi']



class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'

class ChegirmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chegirma
        fields = '__all__'

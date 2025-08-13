from rest_framework import serializers  # DRF serializer base classes
from .models import Product

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

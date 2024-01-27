from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer to parse model object data to Json
    """
    class Meta:
        model = Product
        fields = '__all__'

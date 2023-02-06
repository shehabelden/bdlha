from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)

    class Meta:
        model = CategoryModel
        fields = "__all__"

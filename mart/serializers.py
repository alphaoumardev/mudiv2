from rest_framework import serializers

# from customer.models import *
from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        # fields = ['genre_name']
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        # fields = ['type_name']
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=False, read_only=True)
    type = TypeSerializer(many=False, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'genre', 'type']
        # fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id", "name", "sku", "category", "image", "image_hover",
            "description", "brand", "price", "status", "stock",
            "onsale", "created_at", "updated_at", "deleted_at",
        ]
        # fields  = '__all__'


class ColorsOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorsOption
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class SizeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = SizesOption
        fields = '__all__'


class FuturedImagesSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    color_name = ColorsOptionSerializer(many=False, read_only=True)

    class Meta:
        model = FuturedImages
        fields = ['id', 'image_url', 'product', 'color_name']


class VariantSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    color = ColorsOptionSerializer(many=False, read_only=True)
    size = SizeSerialiser(many=False, read_only=True)

    class Meta:
        model = Variant
        fields = ['id', 'product', 'color', 'size']


class SlidersModel(serializers.ModelSerializer):
    slideItem = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = Sliders
        fields = ['slideItem']

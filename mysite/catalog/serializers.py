from .models import (
    Category, SubCategory, Product,
    ProductImage, Review)
from rest_framework import serializers



class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_image', 'category_name']


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'subcategory_name']


class SubCategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['subcategory_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_categories = SubCategoryListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'sub_categories']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductListSerializer(serializers.ModelSerializer):
    product_img = ProductImageSerializer(many=True, read_only=True)
    created_date = serializers.DateField(format='%d-%m-%Y')
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'product_type', 'price', 'product_name', 'id',
            'product_img', 'created_date','get_avg_rating','get_count_people'
        ]

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self,obj):
        return obj.get_count_people()



class SubCategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ['subcategory_name', 'products']


class ReviewSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    product_img = ProductImageSerializer(many=True, read_only=True)
    created_date = serializers.DateField(format='%d-%m-%Y')
    subcategory = SubCategoryNameSerializer()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'product_name', 'subcategory', 'price', 'product_img',
            'video', 'description', 'article_number', 'product_type',
            'created_date', 'reviews'
        ]


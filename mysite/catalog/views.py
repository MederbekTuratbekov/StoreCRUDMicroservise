from .serializers import (CategoryListSerializer, CategoryDetailSerializer,
                          SubCategoryListSerializer, ProductDetailSerializer, SubCategoryDetailSerializer,
                          ProductImageSerializer, ReviewSerializer, ProductListSerializer)
from .models import (Category,SubCategory,Review,Product,ProductImage)
from rest_framework import viewsets,generics,permissions,status
from .pagination import CategoryPagination,ProductPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filter import Productfilter
from rest_framework.filters import SearchFilter,OrderingFilter

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = CategoryPagination


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class SubCategoryListAPIView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryListSerializer


class SubCategoryDetailAPIEView(generics.RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryDetailSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = Productfilter
    search_fields = ['article_number']
    ordering_fields = ['price', 'created_date']


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


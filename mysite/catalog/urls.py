from django.urls import path,include
from .views import (CategoryListAPIView,ProductListAPIView,CategoryDetailAPIView,
                    SubCategoryDetailAPIEView,ProductDetailAPIView
                     ,SubCategoryListAPIView,ReviewViewSet,ProductImageViewSet)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'review',ReviewViewSet)
router.register(r'product_image',ProductImageViewSet)  # ИЗМЕНЕНО: добавлен роут для загрузки/удаления фото товара


urlpatterns = [
    path('',include(router.urls)),
    path('category/',CategoryListAPIView.as_view(),name='category_list'),
    path('category/<int:pk>/',CategoryDetailAPIView.as_view(),name='category_detail'),
    path('sub_category/',SubCategoryListAPIView.as_view(),name='sub_category'),
    path('sub_category/<int:pk>/',SubCategoryDetailAPIEView.as_view(),name='sub_category_detail'),
    path('product/',ProductListAPIView.as_view(),name='product_list'),
    path('product/<int:pk>/',ProductDetailAPIView.as_view(),name='product_detail'),
]

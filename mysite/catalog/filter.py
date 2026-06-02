from django_filters import FilterSet
from .models import Product

class Productfilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'product_type': ['exact'],
            'price': ['gt','lt'],
        }
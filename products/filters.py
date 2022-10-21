from django_filters import rest_framework as filters, DateRangeFilter

from products.models import Products


class ProductsFilter(filters.FilterSet):
    category = filters.CharFilter(lookup_expr='icontains')
    p_name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Products
        fields = ['category', 'p_name']
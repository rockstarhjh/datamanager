# from django_filters import rest_framework as filters, DateRangeFilter
#
# from stocks.models import Stocks
#
#
# class StocksFilter(filters.FilterSet):
#     date = filters.DateFromToRangeFilter(field_name="date", label="Date (Between)")
#     category = filters.CharFilter(lookup_expr='icontains')
#     p_name = filters.CharFilter(lookup_expr='icontains')
#     company = filters.CharFilter(lookup_expr='icontains')
#
#     class Meta:
#         model = Stocks
#         exclude = ['idproducts', 'in_field', 'out_field', 'return_field', 'lost_field']
#         fields = ['date', 'category', "p_name", 'company']
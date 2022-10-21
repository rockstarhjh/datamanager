from django_filters import rest_framework as filters, DateRangeFilter

from acount.models import Acount


class AcoFilter(filters.FilterSet):
    # date = filters.DateFromToRangeFilter()
    # date = DateRangeFilter(field_name = 'date')
    date = filters.DateFromToRangeFilter(field_name="date", label="Date (Between)")
    company = filters.CharFilter(lookup_expr='icontains')
    product = filters.CharFilter(lookup_expr='icontains')
    division = filters.CharFilter(lookup_expr='exact')
    inoutcompany = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Acount
        fields = ['date', 'company', "product", 'division', 'inoutcompany']

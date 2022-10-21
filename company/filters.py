from django_filters import rest_framework as filters, DateRangeFilter

from company.models import Company


class ComFilter(filters.FilterSet):
    # date = filters.DateFromToRangeFilter()
    # date = DateRangeFilter(field_name = 'date')
    # date = filters.DateFromToRangeFilter(field_name="date", label="Date (Between)")
    company = filters.CharFilter(field_name="name", lookup_expr='contains')
    # product = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Company
        fields = ['company']

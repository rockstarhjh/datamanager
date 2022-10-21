from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class SimpleDataTablePagination(LimitOffsetPagination):
    limit_query_param = 'length'
    offset_query_param = 'start'

    def get_paginated_response(self, data):
        return Response({
            'draw': self.request.GET.get('draw', 1),
            'count': self.count,
            'recordsTotal': self.count,
            'recordsFiltered': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'data': data
        })
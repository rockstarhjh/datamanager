from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, renderers
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_datatables.filters import DatatablesFilterBackend

from acount.pagination import SimpleDataTablePagination
from products.filters import ProductsFilter
from products.models import Products
from products.serializers import ProductSerializer
from stocks.models import Stocks


class ProductsModelViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsAdminUser,)
    filter_backends = [DjangoFilterBackend, DatatablesFilterBackend]
    # filter_backends = DatatablesFilterBackend
    filterset_class = ProductsFilter


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        # print('1')
        # form = StocksForm()
        return Response(template_name='products/products.html')
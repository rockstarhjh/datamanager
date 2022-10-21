from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render, redirect

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, renderers
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework_datatables.filters import DatatablesFilterBackend

from acount.pagination import SimpleDataTablePagination
from price.form import PriceForm
from price.models import Price
from price.serializers import PriceSerializer
from products.models import Products


class PriceModelViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    # permission_classes = (IsAdminUser,)


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        # instance = Products.objects.all()
        # print(instance)
        # product_info = self.serializer_class(instance).data
        # product_info = ProductSerializer(instance)
        # form = PriceForm()
        return Response(template_name='price/price.html')

    # def create(self, request, *args, **kwargs):
    #
    #     serializer = self.get_serializer(data=request.data)
    #     # print(request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     form = PriceForm()
    #     headers = self.get_success_headers(serializer.data)
    #     messages.info(request, '등록되었습니다.')
    #     return redirect('price:price_list')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.serializer_class(instance).data
        # print(data['product'])
        form = PriceForm(data)
        return Response({'data': data, 'form': form}, template_name='price/priceForm.html')

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        print(serializer)

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        form = PriceForm(serializer.data)
        messages.info(request, '수정되었습니다.')
        return Response({'data': serializer.data, 'form': form}, template_name='price/priceForm.html')

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response({'status': True})
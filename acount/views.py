import json
import logging
import os
import sys

from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.template.response import SimpleTemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import renderers, filters
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_datatables.filters import DatatablesFilterBackend

from acount.filters import AcoFilter
from acount.form import AcoForm
from acount.models import Acount
from acount.pagination import SimpleDataTablePagination
from acount.serializers import AcoSerializer


class AcoModelViewSet(ModelViewSet):
    queryset = Acount.objects.all()
    serializer_class = AcoSerializer
    # permission_classes = (IsAdminUser,)
    filter_backends = [DjangoFilterBackend, DatatablesFilterBackend]
    # filterset_fields  = ['date', 'company', 'product']
    # filter_fields = ('date', 'company', 'product')
    filterset_class = AcoFilter


class AcoViewSet(ModelViewSet):
    queryset = Acount.objects.all()
    serializer_class = AcoSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)
    pagination_class = SimpleDataTablePagination

    def list(self, request, *args, **kwargs):
        path = os.path.abspath(__file__)
        print(path)
        print(sys.path)
        path = os.path.abspath(__file__ + '/..')
        print(path)
        if path not in sys.path:
            print(path)
            sys.path.append(path)
            print(sys.path)
        # queryset = self.filter_queryset(self.get_queryset())
        #
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        #
        # serializer = self.get_serializer(queryset, many=True)
        form = AcoForm()
        return Response({'form': form}, template_name='acount/acount.html')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        form = AcoForm()
        headers = self.get_success_headers(serializer.data)
        messages.info(request, '등록되었습니다.')
        return redirect('acount:aco-list')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # print("get")
        # query = request.GET.get('query', None)  # read extra data
        # print(self.serializer_class(instance).data['name'])
        data = self.serializer_class(instance).data
        # print(data)
        form = AcoForm(data)
        return Response({'data': data, 'form': form}, template_name='acount/acoForm.html')

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        # print('업데이트')
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        form = AcoForm(serializer.data)
        messages.info(request, '수정되었습니다.')
        return Response({'data': serializer.data, 'form': form}, template_name='acount/acoForm.html')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        # print(instance.delete())
        # return HttpResponseRedirect(redirect_to='https://google.com')
        return Response({'status': True})


class Transaction(APIView):
    def get(self, request):
        return SimpleTemplateResponse('acount/transaction.html')

    def post(self, request):
        # context = {'data': request.data}
        data = request.data
        product = request.POST.getlist('aco_product')
        count = request.POST.getlist('aco_count')
        unit = request.POST.getlist('aco_unit')
        price = request.POST.getlist('aco_price')
        sumprice = request.POST.getlist('aco_sumprice')
        tax = request.POST.getlist('aco_tax')
        # print(data.sumpricesum)
        sumpricesum = data['aco_sumpricesum']
        taxsum = data['aco_taxsum']
        totalpricesum = data['aco_totalpricesum']
        # print(data['aco_product'])
        return render(request, 'acount/transaction.html',
                      {'data': data, 'product': product, 'count': count, 'unit': unit, 'price': price,
                       'sumprice': sumprice, 'tax': tax, 'sumpricesum': sumpricesum, 'taxsum': taxsum,
                       'totalpricesum': totalpricesum})

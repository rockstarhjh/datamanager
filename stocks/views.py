from django.contrib import messages
from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, renderers
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework_datatables.filters import DatatablesFilterBackend

# from stocks.filters import StocksFilter
from stocks.form import StocksForm
from stocks.models import Stocks
from stocks.serializers import StocksSerializer

# Create your views here.


class StocksModelViewSet(viewsets.ModelViewSet):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer
    # permission_classes = (IsAdminUser,)
    filter_backends = [SearchFilter, DatatablesFilterBackend]


class StocksViewSet(viewsets.ModelViewSet):
    queryset = Stocks.objects.all()
    serializer_class = StocksSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        # print('1')
        form = StocksForm()
        return Response({'form': form}, template_name='stocks/stocks.html')

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        # print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        form = StocksForm()
        headers = self.get_success_headers(serializer.data)
        messages.info(request, '등록되었습니다.')
        return redirect('stocks:stocks_list')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.serializer_class(instance).data
        # print(data['idproducts'])
        form = StocksForm(data)
        return Response({'data': data, 'form': form}, template_name='stocks/stocksForm.html')

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        # print(serializer)

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        form = StocksForm(serializer.data)
        messages.info(request, '수정되었습니다.')
        return Response({'data': serializer.data, 'form': form}, template_name='stocks/stocksForm.html')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        # print(instance.delete())
        # return HttpResponseRedirect(redirect_to='https://google.com')
        return Response({'status': True})

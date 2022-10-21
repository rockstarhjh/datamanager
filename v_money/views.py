from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets, renderers
from rest_framework.response import Response

from v_money.form import VMoneyForm
from v_money.models import VMoney
from v_money.serializers import VMoneySerializer


class VMoneyModelViewSet(viewsets.ModelViewSet):
    queryset = VMoney.objects.all()
    serializer_class = VMoneySerializer
    # filter_backends = [SearchFilter, DatatablesFilterBackend]


class VMoneyViewSet(viewsets.ModelViewSet):
    queryset = VMoney.objects.all()
    serializer_class = VMoneySerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        sumIn = VMoney.objects.aggregate(Sum('deposit')).get('deposit__sum') or 0
        sumOut = VMoney.objects.aggregate(Sum('expense')).get('expense__sum') or 0
        qq = sumIn - sumOut
        form = VMoneyForm()
        return Response({'sum': qq, 'form': form}, template_name='v_money/v_money.html')

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        # print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        form = VMoneyForm()
        headers = self.get_success_headers(serializer.data)
        messages.info(request, '등록되었습니다.')
        return redirect('v_money:v_money_list')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.serializer_class(instance).data
        form = VMoneyForm(data)
        return Response({'data': data, 'form': form}, template_name='v_money/v_moneyForm.html')

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        print(serializer)

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        form = VMoneyForm(serializer.data)
        messages.info(request, '수정되었습니다.')
        return Response({'data': serializer.data, 'form': form}, template_name='v_money/v_moneyForm.html')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'status': True})


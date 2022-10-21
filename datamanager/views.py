import logging
from datetime import datetime, timedelta, date

from dateutil.relativedelta import relativedelta
from django.db.models import Q, Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import render, redirect
from rest_framework import viewsets, renderers
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from acount.models import Acount
from datamanager.models import Notice
from datamanager.serializers import AcountSerializer, NoticeSerializer


class NoticeViewSet(ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = (IsAdminUser,)


class Main(viewsets.ModelViewSet):
    queryset = Acount.objects.all()
    serializer_class = AcountSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)
    # def get_queryset(self):
    #     today = date.today()
    #     yesterday = date.today() - timedelta(1)
    #     queryset = self.queryset
    #     query_set = queryset.filter(Q(date=yesterday) & Q(division="매출") | Q(date=yesterday) & Q(division="매입반품")). \
    #                     aggregate(Sum('totalprice')).get('totalprice__sum') or 0
    #     return query_set

    def list(self, request, *args, **kwargs):
        # today = date.today()
        # yesterday = date.today() - timedelta(1)
        # if not request.user.is_authenticated:
        #     return redirect('user:login')
        # queryset = self.filter_queryset(self.get_queryset())
        tr = self.today_revenue()
        yr = self.yesterday_revenue()
        # revenue_label, revenue_value, r_header = self.month_revenue()
        # purchase_label, purchase_value, p_header = self.month_purchase()
        revenue_label, revenue_value, purchase_label, purchase_value, net_label, net_value = self.month_data(5)
        goal = Notice.objects.order_by('-pk')[0].comment1
        notice = Notice.objects.order_by('-pk')[0].comment2
        # chart = self.monthly_Income(5)

        # print(revenue_value.difference(purchase_value))
        # revenue_label = mr.values_list('month', flat=True)
        # print(revenue_label)
        # revenue_value = mr.values_list('sum', flat=True)
        # print(mr.get(month="2022-10-1")['sum'])
        data = {'tr': tr, 'yr': yr, 'revenue_label': revenue_label, 'revenue_value': revenue_value,
                'r_header': "월별매출", 'purchase_label': purchase_label, 'purchase_value': purchase_value,
                'p_header': "월별매입", 'net_label': net_label, 'net_value': net_value, 'net_header': "월별순이익",
                'goal': goal, 'notice': notice}

        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        # serializer = self.get_serializer(queryset, many=True)

        return Response({'data': data}, template_name='datamanager/index.html')

    def yesterday_revenue(self):
        yesterday = date.today() - timedelta(1)
        queryset = self.queryset
        yesterday_revenue = queryset.filter(
            Q(date=yesterday) & Q(division="매출") | Q(date=yesterday) & Q(division="매입반품")) \
            .aggregate(Sum('sumprice')).get('sumprice__sum') or 0
        return yesterday_revenue

    def today_revenue(self):
        today = date.today()
        queryset = self.queryset
        today_revenue = queryset.filter(Q(date=today) & Q(division="매출") | Q(date=today) & Q(division="매입반품")). \
            aggregate(Sum('sumprice')).get('sumprice__sum') or 0
        return today_revenue

    # def month_revenue(self):
    #     queryset = self.queryset
    #     m = (datetime.today() + relativedelta(months=-5)).strftime("%Y-%m-%d")
    #     m2 = m[:-2] + "01"
    #     # year = datetime.today().year
    #     # month = datetime.today().month - 6
    #     # print(m[:-2]+"01")
    #     sum_query = queryset.filter(Q(date__gte=m2) & Q(division="매출") | Q(date__gte=m2) & Q(division="매입반품")). \
    #         annotate(month=TruncMonth('date')) \
    #         .values('month').annotate(sum=Sum('sumprice')).values('month', 'sum')
    #     label_list = sum_query.values_list('month', flat=True)
    #     value_list = sum_query.values_list('sum', flat=True)
    #     month_list = []
    #     for item in label_list:
    #         month_list.append(str(item)[:-3])
    #     # status_list_account = queryset.filter(Q(date__contains="2022-10") & Q(division="매출")).aggregate(Sum('sumprice')).get('sumprice__sum') or 0 \
    #
    #     # print(revenue_list)
    #     # print(TruncMonth(''))
    #     return month_list, revenue_list, "월별 매출"

    # def month_purchase(self):
    #     queryset = self.queryset
    #     m = (datetime.today() + relativedelta(months=-5)).strftime("%Y-%m-%d")
    #     m2 = m[:-2] + "01"
    #     sum_query = queryset.filter(Q(date__gte=m2) & Q(division="매입") | Q(date__gte=m2) & Q(division="매출반품")). \
    #         annotate(month=TruncMonth('date')) \
    #         .values('month').annotate(sum=Sum('sumprice')).values('month', 'sum')
    #     list = sum_query.values_list('month', flat=True)
    #     purchase_list = sum_query.values_list('sum', flat=True)
    #     month_list = []
    #     for item in list:
    #         month_list.append(str(item)[:-3])
    #     return month_list, purchase_list, "월별 매입"

    def month_data(self, month_gap):
        queryset = self.queryset
        m = (datetime.today() + relativedelta(months=-month_gap)).strftime("%Y-%m-%d")
        m2 = m[:-2] + "01"

        r_query = queryset.filter(Q(date__gte=m2) & Q(division="매출") | Q(date__gte=m2) & Q(division="매입반품")). \
            annotate(month=TruncMonth('date')) \
            .values('month').annotate(sum=Sum('sumprice'))

        p_query = queryset.filter(Q(date__gte=m2) & Q(division="매입") | Q(date__gte=m2) & Q(division="매출반품")). \
            annotate(month=TruncMonth('date')) \
            .values('month').annotate(sum=Sum('sumprice'))
        # net_query = queryset.filter(Q(date__gte=m2) & Q(division="매출") | Q(date__gte=m2) & Q(division="매입반품")). \
        #     annotate(month=TruncMonth('date')) \
        #     .values('month').annotate(sum=Sum('sumprice')).values_list('month', 'sum')
        # net_query = r_query.union(p_query)
        # aa = r_query[0]['month']
        # print(mr.get(month="2022-10-1")['sum'])
        r_month_list = r_query.values_list('month', flat=True)
        r_value_list = r_query.values_list('sum', flat=True)
        r_label_list = []
        for item in r_month_list:
            r_label_list.append(str(item)[:-3])

        p_month_list = p_query.values_list('month', flat=True)
        p_value_list = p_query.values_list('sum', flat=True)
        p_label_list = []
        for item in p_month_list:
            p_label_list.append(str(item)[:-3])

        net_label_list = r_label_list
        net_value_list = []

        for i in range(len(net_label_list)):
            # print(i)
            net_value_list.append(r_value_list[i]-p_value_list[i])

        # if r_label_list.count() > p_label_list.count():
        #     net_count = r_label_list.count()
        #     net_label_list = r_label_list
        # else:
        #     net_count = p_label_list.count()
        #     net_label_list = p_label_list
        # net_value_list = [net_count]
        # for i in range(0, net_count-1):
        #     print(r_label_list[i])
        # print(r_label_list[0])
        # net_value_list = net_query.values_list('sum', flat=True)
        # print(net_value_list)
        # print(r_label_list)
        # print(net_query)
        # print(r_month_list)
        # print(r_value_list)
        # print(p_month_list)
        # print(p_value_list)
        # print(net_label_list)
        # print(net_value_list)
        # month_data_list = zip(r_label_list, r_value_list, p_label_list, p_value_list, net_label_list, net_value_list)
        return r_label_list, r_value_list, p_label_list, p_value_list, net_label_list, net_value_list

    # def monthly_Income(self, month_gap):
    #
    #     queryset = self.queryset
    #     m = (datetime.today() + relativedelta(months=-month_gap)).strftime("%Y-%m-%d")
    #     m2 = m[:-2] + "01"
    #     total_monthly_income = queryset.filter(Q(date__gte=m2) & Q(division="매출") | Q(date__gte=m2) & Q(division="매입반품")). \
    #         annotate(month=TruncMonth('date')) \
    #         .values('month').annotate(sum=Sum('sumprice'))
    #     total_monthly_expenses = queryset.filter(Q(date__gte=m2) & Q(division="매입") | Q(date__gte=m2) & Q(division="매출반품")). \
    #         annotate(month=TruncMonth('date')) \
    #         .values('month').annotate(sum=Sum('sumprice'))
    #     income_expense = zip(total_monthly_income, total_monthly_expenses)
    #
    #     net_monthly_income_list = []
    #
    #     for total_monthly_income, total_monthly_expenses in income_expense:
    #         print(total_monthly_income.get('sum', 0))
    #         print(total_monthly_expenses.get('sum', 0))
    #         # net_monthly_income_list.append(
    #         #     total_monthly_income.get('sum', 0) - total_monthly_expenses.get('sum', 0))
    #
    #     income_list = zip(total_monthly_income, total_monthly_expenses, net_monthly_income_list)
    #
    #     context = {
    #         'income_list': income_list
    #     }
    #     for item in net_monthly_income_list:
    #         print(item)
    #     return 1

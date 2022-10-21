from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db.models import Sum, Q, Count
from django.db.models.functions import TruncMonth, TruncYear
from django.utils.dateparse import parse_date
from rest_framework import viewsets, renderers
from rest_framework.response import Response

from acount.models import Acount
from datamanager.serializers import AcountSerializer


class ChartViewSet(viewsets.ModelViewSet):
    queryset = Acount.objects.all()
    serializer_class = AcountSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        year = queryset.values('date').annotate(year=TruncYear('date')).values('year').annotate(count=Count('id')).order_by('-year')
        # month = queryset.annotate(month=TruncMonth('date')).values('month').annotate(count=Count('id'))
        year_list = []
        # month_list = []
        for item in year:
            year_list.append(str(item['year'])[:-6])
        # print(year_list)
        data = {'year_list': year_list}
        return Response({'data':data}, template_name='chart/chart.html')

    def drawchart(self, request, *args, **kwargs):
        # print('111')
        date = request.POST.get('date')
        gap = int(request.POST.get('gap'))
        division = request.POST.get('division')
        date_division = request.POST.get('date_division')
        if date_division == "year":
            label, value, header = self.year_data(date, gap, division)
        else:
            label, value, header = self.month_data(date, gap, division)

        data = {'label': label, 'value': value, 'header': header}

        # print(request.POST.get('date'))
        # print(request.POST.get('division'))
        return Response({'data': data}, template_name='chart/chart.html')

    def month_data(self, date, gap, division):
        queryset = self.queryset
        # n = datetime.today().strftime("%Y-%m-%d")
        n = parse_date(date + "-12-31")
        m = (n - relativedelta(months=gap)).strftime("%Y-%m-%d")
        m2 = m[:-2] + "01"
        # k = "TruncMonth('date')"
        r_query = queryset.filter(Q(date__gte=m2) & Q(date__lte=n) & Q(division="매출") | Q(date__gte=m2) &
                                  Q(date__lte=n) & Q(division="매입반품")).values('date'). \
            annotate(month=TruncMonth('date')).values('month').annotate(sum=Sum('sumprice')).values('month', 'sum')
        p_query = queryset.filter(Q(date__gte=m2) & Q(date__lte=n) & Q(division="매입") | Q(date__gte=m2) &
                                  Q(date__lte=n) & Q(division="매출반품")).values('date'). \
            annotate(month=TruncMonth('date')).values('month').annotate(sum=Sum('sumprice')).values('month', 'sum')

        r_month_list = r_query.values_list('month', flat=True)
        r_value_list = r_query.values_list('sum', flat=True)
        r_label_list = []
        for item in r_month_list:
            r_label_list.append(str(item)[:-3])

        if division == "매출":
            return r_label_list, r_value_list, "매출"

        p_month_list = p_query.values_list('month', flat=True)
        p_value_list = p_query.values_list('sum', flat=True)
        p_label_list = []
        for item in p_month_list:
            p_label_list.append(str(item)[:-3])

        if division == "매입":
            return p_label_list, p_value_list, "매입"

        net_label_list = r_label_list
        net_value_list = []

        for i in range(len(net_label_list)):
            net_value_list.append(r_value_list[i] - p_value_list[i])

        if division == "순이익":
            return net_label_list, net_value_list, "순이익"
        # print(r_label_list)
        # print(r_value_list)
        # if division == "매출":
        #     return r_label_list, r_value_list
        # elif division == "매입":
        #     return p_label_list, p_value_list
        # else:
        #     return net_label_list, net_value_list
        # return 1

    def year_data(self, date, gap, division):
        queryset = self.queryset
        n = parse_date(date + "-12-31")
        # print(n)
        m = (n - relativedelta(years=gap)).strftime("%Y-%m-%d")
        m2 = m[:-2] + "01"
        # year = queryset.values('date').annotate(year=TruncMonth('date')).values('year').annotate(
        #     count=Count('id')).order_by('-year')
        # print(year)
        r_query = queryset.filter(Q(date__gte=m2) & Q(date__lte=n) & Q(division="매출") | Q(date__gte=m2) &
                                  Q(date__lte=n) & Q(division="매입반품")).values('date'). \
            annotate(year=TruncYear('date')).values('year').annotate(sum=Sum('sumprice')).values('year', 'sum')
        p_query = queryset.filter(Q(date__gte=m2) & Q(date__lte=n) & Q(division="매입") | Q(date__gte=m2) &
                                  Q(date__lte=n) & Q(division="매출반품")). \
            annotate(year=TruncYear('date')).values('year').annotate(sum=Sum('sumprice')).values('year', 'sum')
        # print(r_query)
        # print(p_query)
        r_month_list = r_query.values_list('year', flat=True)
        r_value_list = r_query.values_list('sum', flat=True)
        r_label_list = []
        for item in r_month_list:
            r_label_list.append(str(item)[:-6])

        if division == "매출":
            return r_label_list, r_value_list, "매출"

        p_month_list = p_query.values_list('year', flat=True)
        p_value_list = p_query.values_list('sum', flat=True)
        p_label_list = []
        for item in p_month_list:
            p_label_list.append(str(item)[:-3])

        if division == "매입":
            return p_label_list, p_value_list, "매입"

        net_label_list = r_label_list
        net_value_list = []

        for i in range(len(net_label_list)):
            net_value_list.append(r_value_list[i] - p_value_list[i])

        if division == "순이익":
            return net_label_list, net_value_list, "순이익"

        # print(r_label_list)
        # print(r_value_list)
        # return r_label_list, r_value_list, "매출"

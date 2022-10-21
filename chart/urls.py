from django.urls import path, include
from rest_framework.routers import DefaultRouter

from chart.views import ChartViewSet
from stocks.views import StocksModelViewSet, StocksViewSet

app_name = "chart"
Chart = ChartViewSet.as_view({
    'get': 'list',
    'post': 'drawchart',
})
urlpatterns = [
    path('', Chart, name='Chart'),
]
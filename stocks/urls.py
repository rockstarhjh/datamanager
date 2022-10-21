from django.urls import path, include
from rest_framework.routers import DefaultRouter

from stocks.views import StocksModelViewSet, StocksViewSet

app_name = "stocks"

router = DefaultRouter()

router.register('api', StocksModelViewSet)

stocks_list = StocksViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
stocks_detail = StocksViewSet.as_view({
    'get': 'retrieve',
    'post': 'update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', stocks_list, name='stocks_list'),
    path('', include(router.urls), name='stocks'),
    path('<int:pk>/', stocks_detail, name='stocks_detail'),
]
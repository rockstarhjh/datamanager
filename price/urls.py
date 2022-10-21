from django.urls import path, include
from rest_framework.routers import DefaultRouter

from price.views import PriceModelViewSet, PriceViewSet

app_name = "price"

router = DefaultRouter()

router.register('api', PriceModelViewSet)

price_list = PriceViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
price_detail = PriceViewSet.as_view({
    'get': 'retrieve',
    'post': 'update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', PriceViewSet.as_view({'get': 'list'}), name='price_list'),
    path('', include(router.urls), name='price'),
    path('<int:pk>/', price_detail, name='price_detail'),
]
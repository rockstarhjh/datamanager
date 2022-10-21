from django.urls import path, include
from rest_framework.routers import DefaultRouter

from v_money.views import VMoneyModelViewSet, VMoneyViewSet

app_name = "v_money"

router = DefaultRouter()

router.register('api', VMoneyModelViewSet)

v_money_list = VMoneyViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
v_money_detail = VMoneyViewSet.as_view({
    'get': 'retrieve',
    'post': 'update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', v_money_list, name='v_money_list'),
    path('', include(router.urls), name='VMoney'),
    path('<int:pk>/', v_money_detail, name='v_money_detail'),
]
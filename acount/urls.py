from django.urls import path, include
from rest_framework.routers import DefaultRouter

from acount.views import AcoModelViewSet, AcoViewSet, Transaction

app_name = "acount"

router = DefaultRouter()

router.register('api', AcoModelViewSet)

aco_list = AcoViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
aco_detail = AcoViewSet.as_view({
    'get': 'retrieve',
    'post': 'update',
    # 'put': 'update',
    # 'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [

    # path('', views.ComHome.as_view(), name="com-list"),
    # path('', views.ComHome.as_view(), name='com-list'),
    path('', aco_list, name='aco-list'),
    path('', include(router.urls), name='aco'),
    path('<int:pk>/', aco_detail, name='aco-detail'),
    path('transaction/', Transaction.as_view(), name='transaction'),
    # path('<int:pk>/', views.ComDetail.as_view(), name='com-detail'),

    # path('', views.ComViewSet.as_view({'get': 'list'}), basename='company'),
]

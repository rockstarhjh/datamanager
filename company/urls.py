from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComViewSet, ComModelViewSet
from company import views

app_name = "company"

router = DefaultRouter()

router.register('api', ComModelViewSet)

com_list = ComViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
com_detail = ComViewSet.as_view({
    'get': 'retrieve',
    'post': 'update',
    # 'put': 'update',
    # 'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [

    # path('', views.ComHome.as_view(), name="com-list"),
    # path('', views.ComHome.as_view(), name='com-list'),
    path('', com_list, name='com-list'),
    path('', include(router.urls), name='com'),
    path('<int:pk>/', com_detail, name='com-detail'),
    # path('<str:name>/', views.ComList.as_view(), name='com-name'),

    # path('', views.ComViewSet.as_view({'get': 'list'}), basename='company'),
]

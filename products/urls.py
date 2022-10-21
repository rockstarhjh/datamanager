from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import ProductsModelViewSet, ProductsViewSet

app_name = "products"

router = DefaultRouter()

router.register('api', ProductsModelViewSet)

urlpatterns = [
    path('', ProductsViewSet.as_view({'get': 'list'}), name='products_list'),
    path('', include(router.urls), name='products'),
    # path('<int:pk>/', com_detail, name='com-detail'),
]
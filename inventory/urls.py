from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, StockTransactionViewSet, inventory_summary

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('transactions', StockTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('inventory/', inventory_summary, name='inventory-summary'),
]

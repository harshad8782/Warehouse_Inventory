from django.contrib import admin
from django.urls import path, include
from inventory.views import dashboard, transactions_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('inventory.urls')),
    path('', dashboard, name='dashboard'),  # This serves the dashboard
    path('transactions/', transactions_view, name='transactions'),
]

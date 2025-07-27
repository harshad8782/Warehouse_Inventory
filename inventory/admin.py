from django.contrib import admin
from .models import Product, StockTransaction, StockDetail

# Inline editing for StockDetail inside StockTransaction
class StockDetailInline(admin.TabularInline):
    model = StockDetail
    extra = 1  # allow adding details directly in StockTransaction admin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sku', 'created_at')
    search_fields = ('name', 'sku')
    list_filter = ('created_at',)

@admin.register(StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference_no', 'transaction_type', 'created_at')
    list_filter = ('transaction_type', 'created_at')
    search_fields = ('reference_no',)
    inlines = [StockDetailInline]

@admin.register(StockDetail)
class StockDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'transaction', 'product', 'quantity')
    list_filter = ('transaction__transaction_type',)

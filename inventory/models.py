from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):  # maps to prodmast
    name = models.CharField(max_length=100, unique=True)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'prodmast'


class StockTransaction(models.Model):  # maps to stckmain
    TRANSACTION_TYPES = (
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
    )
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    reference_no = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'stckmain'


class StockDetail(models.Model):  # maps to stckdetail
    transaction = models.ForeignKey(StockTransaction, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        db_table = 'stckdetail'
        unique_together = ('transaction', 'product')

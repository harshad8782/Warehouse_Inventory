from rest_framework import serializers
from .models import Product, StockTransaction, StockDetail

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class StockDetailSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = StockDetail
        fields = ['product', 'product_name', 'quantity']

class StockTransactionSerializer(serializers.ModelSerializer):
    details = StockDetailSerializer(many=True)

    class Meta:
        model = StockTransaction
        fields = ['id', 'transaction_type', 'reference_no', 'created_at', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        transaction = StockTransaction.objects.create(**validated_data)
        for detail in details_data:
            StockDetail.objects.create(transaction=transaction, **detail)
        return transaction

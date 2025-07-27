from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Product, StockTransaction, StockDetail
from .serializers import ProductSerializer, StockTransactionSerializer

# API ViewSets
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class StockTransactionViewSet(viewsets.ModelViewSet):
    queryset = StockTransaction.objects.all().prefetch_related('details')
    serializer_class = StockTransactionSerializer

@api_view(['GET'])
def inventory_summary(request):
    products = Product.objects.all()
    inventory_data = []
    for product in products:
        stock_in = StockDetail.objects.filter(product=product, transaction__transaction_type='IN').aggregate(total=Sum('quantity'))['total'] or 0
        stock_out = StockDetail.objects.filter(product=product, transaction__transaction_type='OUT').aggregate(total=Sum('quantity'))['total'] or 0
        inventory_data.append({
            'product': product.name,
            'sku': product.sku,
            'stock': stock_in - stock_out
        })
    return Response(inventory_data)

# Dashboard View (for HTML page)
def dashboard(request):
    inventory = []
    for product in Product.objects.all():
        stock_in = StockDetail.objects.filter(product=product, transaction__transaction_type='IN').aggregate(total=Sum('quantity'))['total'] or 0
        stock_out = StockDetail.objects.filter(product=product, transaction__transaction_type='OUT').aggregate(total=Sum('quantity'))['total'] or 0
        inventory.append({'product': product.name, 'sku': product.sku, 'stock': stock_in - stock_out})
    return render(request, 'dashboard.html', {'inventory': inventory})
from django.shortcuts import redirect
from django.contrib import messages

def transactions_view(request):
    products = Product.objects.all()
    transactions = StockTransaction.objects.prefetch_related('details').order_by('-created_at')

    if request.method == 'POST':
        transaction_type = request.POST.get('transaction_type')
        reference_no = request.POST.get('reference_no')
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        # Validation
        if not transaction_type or not reference_no or not product_id or not quantity:
            messages.error(request, "All fields are required.")
            return redirect('transactions')

        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            messages.error(request, "Quantity must be a positive integer.")
            return redirect('transactions')

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            messages.error(request, "Invalid product selected.")
            return redirect('transactions')

        # Create transaction and detail
        txn = StockTransaction.objects.create(transaction_type=transaction_type, reference_no=reference_no)
        StockDetail.objects.create(transaction=txn, product=product, quantity=quantity)
        messages.success(request, "Transaction added successfully!")
        return redirect('transactions')

    return render(request, 'transactions.html', {
        'products': products,
        'transactions': transactions
    })

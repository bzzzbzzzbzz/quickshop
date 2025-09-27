from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    """Главная страница со списком всех товаров"""
    products = Product.objects.all().order_by('-created_at') # Сортировка от новых к старым
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)

def product_detail(request, product_id):
    """Страница одного товара"""
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)
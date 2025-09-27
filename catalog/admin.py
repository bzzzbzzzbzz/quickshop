from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at') # Что показывать в списке
    list_filter = ('category', 'created_at') # Фильтры справа
    search_fields = ('name', 'description') # Поиск по названию и описанию
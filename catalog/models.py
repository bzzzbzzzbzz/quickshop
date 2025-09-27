from django.db import models


class Product(models.Model):
    # Основные поля
    name = models.CharField(max_length=200, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    # Поле для изображения. Для простоты изображения будут сохраняться в папке 'products/'
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")

    # Тип товара (Powerbank или Headphones)
    CATEGORY_CHOICES = [
        ('POWERBANK', 'Повербанк'),
        ('HEADPHONES', 'Наушники'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Категория")

    # Дата создания (автоматически проставляется при создании)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
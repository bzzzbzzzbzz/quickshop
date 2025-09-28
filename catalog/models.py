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

    def get_price_display(self):
        """Возвращает цену в красивом формате"""
        return f"{self.price} ₽"

    def get_price_huf(self):
        """Возвращает цену в формате HUF"""
        return f"{self.price:,} HUF".replace(",", " ")


    def get_short_description(self):
        """Короткое описание для карточек"""
        return self.description[:100] + '...' if len(self.description) > 100 else self.description

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


    def __str__(self):
        return self.name



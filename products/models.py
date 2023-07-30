from django.db import models


# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
        verbose_name='Название категории товаров'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание категории'
    )


class Product(models.Model):
    name = models.CharField(
        max_length=256
    )
    description = models.TextField(
        verbose_name='Описание товара'
    )
    price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name='Цена товара'
    )
    quantity = models.PositiveBigIntegerField(
        default=0,
        verbose_name='Количество товара'
    )
    image = models.ImageField(
        upload_to='products_images'
    )
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name='category'
    )

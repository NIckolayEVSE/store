from django.db import models

# Create your models here.
from users.models import Users


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

    class Meta:
        verbose_name = 'Категорию товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название товара'
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
        upload_to='products_images',
        verbose_name='Фото товара'
    )
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name='category',
        verbose_name='Название категории'
    )

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name + ": " + f'{self.category.pk}'


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum([x.sum() for x in self])

    def total_quantity(self):
        return sum([x.quantity for x in self])


class Basket(models.Model):
    user = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE,
        verbose_name='Покупатель',
        related_name='buyer'
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт',
        related_name='product'
    )
    quantity = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Количество товаров в корзине'
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время добавления товара в корзину'
    )
    objects = BasketQuerySet.as_manager()

    class Meta:
        verbose_name = 'Корзину'
        verbose_name_plural = 'Козины'

    def __str__(self):
        return f'Корзина для {self.user.first_name} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

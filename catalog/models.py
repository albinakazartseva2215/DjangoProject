from django.db import models

from users.models import User


class Category(models.Model):
    """Модель категории с заданными полями и мета классом"""
    category_name = models.CharField(max_length=100, verbose_name="Наименование", help_text="Введите наименование")
    description = models.TextField(verbose_name="Описание", help_text="Введите описание", blank=True, null=True)

    def __str__(self):
        """Строковое представление класса"""
        return self.category_name

    class Meta:
        """Meta класс, который задает конфигурационные параметры"""
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["category_name"]


class Product(models.Model):
    """Модель продукта с заданными полями и мета классом"""
    product_name = models.CharField(max_length=100, verbose_name="Наименование", help_text="Введите наименование")
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="photos/",
        verbose_name="Изображение",
        help_text="Загрузите изображение",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="products",
        help_text="Введите наименование категории",
        verbose_name="Категория",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за покупку",
        help_text="Введите цену",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
        blank=True,
        null=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату изменения",
        blank=True,
        null=True,
    )
    is_published = models.BooleanField(
        verbose_name='Признак публикации',
        default=False,
        help_text='Отметьте для публикации продукт',
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Введите владельца продукта",
        verbose_name="Владелец продукта",
    )

    def __str__(self):
        """Строковое представление класса"""
        return self.product_name

    class Meta:
        """Meta класс, который задает конфигурационные параметры"""
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["product_name"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

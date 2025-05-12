from django.db import models


class Category(models.Model):
    category_name = models.CharField(
        max_length=100, verbose_name="Наименование", help_text="Введите наименование"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание", blank=True, null=True
    )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["category_name"]


class Product(models.Model):
    product_name = models.CharField(
        max_length=100, verbose_name="Наименование", help_text="Введите наименование"
    )
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

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["product_name"]

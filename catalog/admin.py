from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс администрирования позволяет контролировать отображение и поведение модели Category
    в интерфейсе администратора"""
    # какие поля будут показаны в списке объектов
    list_display = (
        "id",
        "category_name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс администрирования позволяет контролировать отображение и поведение модели Product
        в интерфейсе администратора"""
    # какие поля будут показаны в списке объектов
    list_display = (
        "id",
        "product_name",
        "price",
        "category",
    )
    # по какому полю фильтрация
    list_filter = ("category",)
    search_fields = (
        "product_name",
        "description",
    )

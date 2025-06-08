from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Класс администрирования позволяет контролировать отображение и поведение модели Article
        в интерфейсе администратора"""
    # какие поля будут показаны в списке объектов
    list_display = (
        "id",
        "title",
        "description",
        "image",
        "views_count"
    )
    # по какому полю фильтрация
    list_filter = ("title",)
    search_fields = (
        "title",
        "description",
    )

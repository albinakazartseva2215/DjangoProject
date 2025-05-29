from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "image",
        "views_count"
    )
    list_filter = ("title",)
    search_fields = (
        "title",
        "description",
    )

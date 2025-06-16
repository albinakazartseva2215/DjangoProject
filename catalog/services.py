from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """Метод получает список продуктов из кэша. Если нет, то из базы данных"""
    if not CACHE_ENABLED:
        return Product.objects.all()

    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(pk):
    products = Product.objects.filter(category_id=pk).select_related("category")
    return products

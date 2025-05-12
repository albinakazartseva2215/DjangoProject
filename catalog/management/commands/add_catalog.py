from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        call_command("loaddata", "catalog_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
        # category3, _ = Category.objects.get_or_create(category_name='Холодильники', description='Cовременное и функциональное решение для хранения продуктов')
        #
        # products = [
        #     {'product_name': 'Indesit ITS 5200 NG No Frost', 'description': 'Серый цвет, двухкамерный', 'image': 'catalog/image/photo/indesit.jpg', 'category': category3, 'price': '55000', 'created_at': '2025-05-11', 'updated_at': '2025-05-11'},
        # ]
        #
        # for product_data in products:
        #     product, created = Product.objects.get_or_create(**product_data)
        #     if created:
        #         self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.product_name}'))
        #     else:
        #         self.stdout.write(self.style.WARNING(f'Product already exists: {product.first_name}'))

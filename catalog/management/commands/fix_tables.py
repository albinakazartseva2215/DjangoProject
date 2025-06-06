from django.core.management.base import BaseCommand
from django.db import connection
from django.apps import apps


class Command(BaseCommand):
    help = 'Create missing database tables'

    def handle(self, *args, **options):
        # Получаем список существующих таблиц
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """)
            existing_tables = [row[0] for row in cursor.fetchall()]

        # Создаём отсутствующие таблицы
        created_count = 0
        for model in apps.get_models():
            table_name = model._meta.db_table
            if table_name not in existing_tables:
                try:
                    with connection.schema_editor() as schema_editor:
                        schema_editor.create_model(model)
                    self.stdout.write(self.style.SUCCESS(f'✓ Создана таблица: {table_name}'))
                    created_count += 1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'✗ Ошибка создания {table_name}: {str(e)}'))

        if created_count == 0:
            self.stdout.write(self.style.SUCCESS('✓ Все таблицы уже существуют'))
        else:
            self.stdout.write(self.style.SUCCESS(f'✓ Создано таблиц: {created_count}'))

        # Добавьте в конец функции handle
        self.stdout.write("\nПроверка всех моделей:")
        for model in apps.get_models():
            table_name = model._meta.db_table
            with connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}')")
                exists = cursor.fetchone()[0]
            status = "✓" if exists else "✗"
            self.stdout.write(f"{status} {table_name}")
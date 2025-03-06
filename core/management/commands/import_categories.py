import json
from django.core.management.base import BaseCommand
from core.models import Category  # Импортируем модель Category

class Command(BaseCommand):
    help = 'Import categories from JSON'

    def handle(self, *args, **kwargs):
        with open('scripts_data/data.json', 'r') as file:  # Указываем путь к файлу
            data = json.load(file)

            for category_data in data:
                if category_data['model'] == 'core.category':  # Проверяем, что это категория
                    fields = category_data['fields']
                    category_id = category_data['pk']
                    category_name = fields['name']
                    
                    # Попробуем найти категорию по имени
                    category = Category.objects.filter(name=category_name).first()
                    
                    if category:
                        # Если категория найдена, обновим поля description и image
                        category.description = fields['description']
                        category.image = fields['image']
                        category.save()
                        self.stdout.write(self.style.WARNING(f'Category {category.name} updated'))

        self.stdout.write(self.style.SUCCESS('Categories successfully imported'))

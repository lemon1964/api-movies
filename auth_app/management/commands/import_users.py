import json
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

User = get_user_model()

class Command(BaseCommand):
    help = 'Import users from JSON'

    def handle(self, *args, **kwargs):
        with open('scripts_data/users_export.json', 'r') as file:  # Указываем путь к файлу
            data = json.load(file)

            for user_data in data:
                # Извлекаем данные пользователя из JSON
                fields = user_data['fields']
                try:
                    # Создаем пользователя с учетом кастомных полей
                    user = User(
                        id=user_data['pk'],
                        email=fields['email'],
                        username=fields['username'],
                        first_name=fields['first_name'],
                        last_name=fields['last_name'],
                        is_staff=fields['is_staff'],
                        is_superuser=fields['is_superuser'],
                        is_active=fields['is_active'],
                        date_joined=fields['date_joined'],
                        name=fields['name'],
                        provider=fields['provider'],
                        newsletter=fields['newsletter'],
                        points=fields['points'],
                    )
                    
                    # Присваиваем зашифрованный пароль
                    user.password = fields['password']
                    # user.password = fields['password']
                    user.save()

                    self.stdout.write(self.style.SUCCESS(f'Successfully imported user {user.email}'))

                except IntegrityError as e:
                    self.stdout.write(self.style.ERROR(f'Error importing user {fields["email"]}: {str(e)}'))

        self.stdout.write(self.style.SUCCESS('All users successfully imported'))

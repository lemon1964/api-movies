import requests
from django.core.management.base import BaseCommand
from core.models import Category, Movie
from decouple import config

API_KEY = config('API_KEY')
BASE_URL = 'https://www.omdbapi.com/'

class Command(BaseCommand):
    help = 'Load movies from OMDb API'

    def handle(self, *args, **kwargs):
        categories = [
            'Love', 'Life', 'Battle', 'Party', 'Mystery',
            'Adventure', 'Journey', 'Dream', 'War', 'Hero'
        ]

        limit = 10  # Ограничение количества фильмов на категорию

        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)

            params = {
                'apikey': API_KEY,
                's': category_name,
                'type': 'movie'
            }
            response = requests.get(BASE_URL, params=params)
            data = response.json()

            movies_loaded = 0
            for item in data.get('Search', []):
                if movies_loaded >= limit:
                    break

                movie, created = Movie.objects.get_or_create(
                    title=item['Title'],
                    type=item['Type'],
                    category=category,
                    imdb_id=item['imdbID'],
                    defaults={
                        'poster': item.get('Poster', ''),
                        'year': item.get('Year', '')
                    }
                )

                if created:
                    movies_loaded += 1
                    self.stdout.write(self.style.SUCCESS(f'Successfully added movie: {movie.title}'))

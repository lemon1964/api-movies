from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/auth/', include('auth_app.urls')),  # Все пути auth перенесены в auth_app.urls
    path('accounts/', include('allauth.urls')),  # Пути для верификации email    

    path('api/', include('core.urls')),
    path('', lambda request: HttpResponse("Welcome to Django Auth Module!")),
]


# cd api
# python manage.py runserver

# cd react-movies
# cd src
# npm start

# python manage.py makemigrations
# python manage.py migrate

# pip install -U -r requirements.txt    в проект
# pip freeze > requirements.txt         из проекта

# git remote -v

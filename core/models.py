from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=25, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)  # Вместо description
    category = models.ForeignKey(Category, related_name='movies', on_delete=models.CASCADE)
    poster = models.URLField(blank=True, null=True)
    imdb_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title

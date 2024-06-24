from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, MovieViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

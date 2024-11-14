from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.poem.views import PoemViewSet
from apps.poet.views import PoetViewSet
from apps.verse.views import VerseViewSet
from apps.collection.views import CollectionViewSet


router = DefaultRouter()
router.register(r'poet', PoetViewSet)
router.register(r'poem', PoemViewSet)
router.register(r'collection', CollectionViewSet)
router.register(r'verse',VerseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
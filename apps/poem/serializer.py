from rest_framework import serializers

from .models import Poem

from apps.verse.models import Verse
from apps.verse.serializer import VerseSerializer

from apps.collection.serializer import CollectionListSerializer


class PoemDetailSerializer(serializers.ModelSerializer):
    collection = CollectionListSerializer(read_only=True)
    verses = serializers.SerializerMethodField()

    class Meta:
        model = Poem
        fields = '__all__'

    @staticmethod
    def get_verses(obj):
        verses = Verse.objects.filter(poem=obj)
        return VerseSerializer(verses, many=True).data


class PoemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = '__all__'


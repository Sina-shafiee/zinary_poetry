from rest_framework import serializers
from .models import Collection

from apps.poem.models import Poem


class PoemInCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ['title', 'id', 'poet_id']


class CollectionDetailSerializer(serializers.ModelSerializer):
    poems = serializers.SerializerMethodField()

    class Meta:
        model = Collection
        fields = '__all__'

    @staticmethod
    def get_poems(obj):
        poems = Poem.objects.filter(collection=obj)
        return PoemInCollectionSerializer(poems, many=True).data


class CollectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

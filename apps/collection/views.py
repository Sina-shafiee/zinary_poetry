from rest_framework import viewsets
from api.permissions import IsWriterOrReadOnly

from .models import Collection
from .serializer import CollectionListSerializer, CollectionDetailSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CollectionDetailSerializer
        return CollectionListSerializer


    permission_classes = [IsWriterOrReadOnly]

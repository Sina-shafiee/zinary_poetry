from rest_framework import viewsets
from .models import Poem
from .serializer import PoemDetailSerializer, PoemListSerializer
from api.permissions import IsWriterOrReadOnly

class PoemViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PoemDetailSerializer
        return PoemListSerializer

    permission_classes = [IsWriterOrReadOnly]
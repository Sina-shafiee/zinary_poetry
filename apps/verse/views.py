from rest_framework import viewsets
from .models import Verse
from .serializer import VerseSerializer
from api.permissions import IsWriterOrReadOnly

class VerseViewSet(viewsets.ModelViewSet):
    queryset = Verse.objects.all()
    serializer_class = [VerseSerializer]

    permission_classes = [IsWriterOrReadOnly]
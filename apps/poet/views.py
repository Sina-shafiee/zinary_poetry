from rest_framework import viewsets
from .models import Poet
from .serializer import PoetSerializer
from api.permissions import IsWriterOrReadOnly

class PoetViewSet(viewsets.ModelViewSet):
    queryset = Poet.objects.all()
    serializer_class = PoetSerializer

    permission_classes = [IsWriterOrReadOnly]
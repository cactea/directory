from rest_framework import viewsets

from .serializers import CacteaSerializer
from .models import cactea


class CacteaViewSet(viewsets.ModelViewSet):
    queryset = cactea.objects.all()
    serializer_class = CacteaSerializer

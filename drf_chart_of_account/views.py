"""Chart of Accounts View Classes."""
from rest_framework import viewsets
from .serializers import LayerOneModelSerializer


# Create your views here.
class LayerOneModelViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for viewing and editing accounts."""

    serializer_class = LayerOneModelSerializer
    queryset = serializer_class.Meta.model.objects.all()

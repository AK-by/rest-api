from rest_framework import viewsets
from . serializers import SimpleMessagesSerializer
from . models import SimpleMessages


class SimpleMessagesApiListView(viewsets.ModelViewSet):
    serializer_class = SimpleMessagesSerializer
    queryset = SimpleMessages.objects.all().order_by('pk')

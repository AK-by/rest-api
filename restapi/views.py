from django_filters import rest_framework as filters
from rest_framework import viewsets
from . serializers import SimpleMessagesSerializer
from . models import SimpleMessages
from . filters import MessageFilter


class SimpleMessagesApiListView(viewsets.ModelViewSet):
    serializer_class = SimpleMessagesSerializer
    queryset = SimpleMessages.objects.all().order_by('pk')
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = MessageFilter

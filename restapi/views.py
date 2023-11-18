from django_filters import rest_framework as dj_filters
from rest_framework import viewsets, filters
from . serializers import SimpleMessagesSerializer
from . models import SimpleMessages
from . filters import MessageFilter


class SimpleMessagesApiListView(viewsets.ModelViewSet):
    serializer_class = SimpleMessagesSerializer
    queryset = SimpleMessages.objects.all().order_by('pk')
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter, )
    filterset_class = MessageFilter
    ordering_fields = ("id", "title", "created", )
    ordering = ("-created", )
    search_fields = ("id", "title", "message", )
    # search_fields = ("id", "title", "message", "author__name")  # Если через связь к таблице

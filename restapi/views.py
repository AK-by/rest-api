from django_filters import rest_framework as dj_filters
from rest_framework import viewsets, filters
from . serializers import SimpleMessagesSerializer
from . models import SimpleMessages
from . filters import MessageFilter
from . pagination import MessagePagination


class SimpleMessagesApiListView(viewsets.ModelViewSet):
    serializer_class = SimpleMessagesSerializer
    queryset = SimpleMessages.objects.all().order_by('pk')

    # Filters
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter, )
    filterset_class = MessageFilter

    # Ordering
    ordering_fields = ("id", "title", "created", )
    ordering = ("-created", )

    # Search
    search_fields = ("id", "title", "message", )
    # search_fields = ("id", "title", "message", "author__name")  # Если через связь к таблице

    # Pagination
    # Глобальная настройка прописана в settings.py
    # Ниже ручная настройка
    pagination_class = MessagePagination

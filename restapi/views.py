from django_filters import rest_framework as dj_filters
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from . serializers import SimpleMessagesSerializer, SimpleMessagesImagesSerializer
from . models import SimpleMessages
from . filters import MessageFilter
from . pagination import MessagePagination


class SimpleMessagesApiListView(viewsets.ModelViewSet):
    queryset = SimpleMessages.objects.all()
    serializer_class = SimpleMessagesSerializer
    serializer_classes = {
        "list": SimpleMessagesSerializer,
        "create": SimpleMessagesSerializer,
        "retrieve": SimpleMessagesSerializer,
        "update": SimpleMessagesSerializer,
        "recent_messages": SimpleMessagesSerializer,
        "update_image": SimpleMessagesImagesSerializer,
    }

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

    @action(detail=True, methods=["get"], url_path="update-image")
    def update_image(self, request, pk=None):
        message = self.get_object()
        serializer = self.serializer_classes.get(self.action, self.serializer_class)(message, request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            message.image.delete(save=True)
            # message.image = request.data['image'] # Будет в patch / put
            self.perform_update(serializer)

        return Response(serializer.data)
